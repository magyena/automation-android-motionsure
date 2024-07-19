import psycopg2
import time
from sshtunnel import SSHTunnelForwarder


def get_otp_from_db(identity):
    conn = None
    tunnel = None
    try:
        # Set up the SSH tunnel
        tunnel = SSHTunnelForwarder(
            ("108.137.34.236", 22),
            ssh_username="ubuntu",
            ssh_pkey="/Users/fatahalim/Documents/Vision+/automation-android-python/MiradaVersion/utils/p-kp-jumphost-db.pem",  # Path to your private key
            remote_bind_address=(
                "p-bss-cluster.cluster-crghkxvi5das.ap-southeast-3.rds.amazonaws.com",
                5432,
            ),
        )

        # Start the tunnel
        tunnel.start()

        # Connect to the PostgreSQL database through the SSH tunnel
        conn = psycopg2.connect(
            dbname="otp",
            user="team_qa",
            password="4321lupa",
            host="127.0.0.1",
            port=tunnel.local_bind_port,
        )
        time.sleep(2)

        # Create a cursor object using a context manager
        with conn.cursor() as cursor:
            # Using a placeholder for the phone number to prevent SQL injection
            query = """
            SELECT otp 
            FROM public.otps 
            WHERE recipient LIKE %s 
              AND verified = false 
            ORDER BY created_at DESC 
            LIMIT 1;
            """

            cursor.execute(query, ("%" + identity + "%",))

            last_otp = cursor.fetchone()
            # print(last_otp[0])
            if last_otp:
                return last_otp[0]
            else:
                return None

    except Exception as error:
        print(f"Error fetching OTP: {error}")
        return None

    finally:
        if conn:
            conn.close()
        if tunnel:
            tunnel.stop()


def get_last_otp_prod(identity):
    # print(identity)
    conn = None
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="otp",
            user="team_qa",
            password="4321lupa",
            host="10.10.20.20",
            port="5432",
        )
        time.sleep(2)
        # Create a cursor object using a context manager
        with conn.cursor() as cursor:
            # Using a placeholder for the phone number to prevent SQL injection
            query = """
            SELECT otp 
            FROM public.otps 
            WHERE recipient LIKE %s 
              AND verified = false 
            ORDER BY created_at DESC 
            LIMIT 1;
            """

            cursor.execute(query, ("%" + identity + "%",))

            last_otp = cursor.fetchone()

            if last_otp:
                return last_otp[0]
            else:
                return None

    except Exception as error:
        print(f"Error fetching OTP: {error}")
        return None

    finally:
        if conn:
            conn.close()


# def main():
#     identity = "qa8083@visionplus.id"
#     otp = get_last_otp_prod(identity)
#     if otp:
#         print(f"OTP for {identity}: {otp}")
#     else:
#         print(f"No OTP found for {identity}")

#     return otp

# if _name_ == "_main_":
#     main()
