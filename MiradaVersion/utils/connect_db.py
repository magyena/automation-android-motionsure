import psycopg2
import time

def get_last_otp(phone_number):
    # print("Phone number in DB:", phone_number)
    conn = None
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            dbname="otp",
            user="team_qa",
            password="4321lupa",
            host="10.10.20.20",
            port="5432"
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
            
            cursor.execute(query, ('%' + phone_number + '%',))
            
          
            last_otp = cursor.fetchone()
            

            if last_otp:
                # print("OTP in DB:", last_otp[0])
                return last_otp[0]
            else:
                print("No OTP found")
                return None

    except Exception as error:
        print(f"Error fetching OTP: {error}")
        return None
    
    finally:
        
        if conn:
            conn.close()
