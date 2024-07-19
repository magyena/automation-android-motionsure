import psycopg2
import paramiko
import time
import logging
from sshtunnel import SSHTunnelForwarder

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_otp_from_db(phone_number):
    ssh_host = "108.137.34.236"
    ssh_port = 22
    ssh_user = "ubuntu"
    ssh_key = "/Users/fatahalim/Documents/Vision+/automation-android-python/MiradaVersion/utils/p-kp-jumphost-db.pem"

    db_host = "p-bss-cluster.cluster-crghkxvi5das.ap-southeast-3.rds.amazonaws.com"
    db_port = 5432
    db_name = "otp"
    db_user = "team_qa"
    db_password = "4321lupa"

    conn = None
    try:
        # Establish the SSH tunnel
        with SSHTunnelForwarder(
            (ssh_host, ssh_port),
            ssh_username=ssh_user,
            ssh_pkey=ssh_key,
            remote_bind_address=(db_host, db_port),
        ) as tunnel:

            # Connect to the PostgreSQL database through the tunnel
            conn = psycopg2.connect(
                dbname=db_name,
                user=db_user,
                password=db_password,
                host="127.0.0.1",
                port=tunnel.local_bind_port,
            )
            time.sleep(2)

            # Create a cursor object using a context manager
            with conn.cursor() as cursor:
                query = """
                SELECT otp 
                FROM public.otps 
                WHERE recipient LIKE %s 
                  AND verified = false 
                ORDER BY created_at DESC 
                LIMIT 1;
                """

                cursor.execute(query, ("%" + phone_number + "%",))
                last_otp = cursor.fetchone()

                if last_otp:
                    logger.info(f"OTP in DB: {last_otp[0]}")
                    return last_otp[0]
                else:
                    logger.info("No OTP found")
                    return None

    except Exception as error:
        logger.error(f"Error fetching OTP: {error}")
        return None

    finally:
        if conn:
            conn.close()
