# LAB 5 - STUDENT FEE CALCULATION USING FUNCTIONS

def fee_management():

    def calculate_fee(tuition_fee,
                      hostel_fee=0,
                      transportation_fee=0):

        total_fee = tuition_fee + hostel_fee + transportation_fee

        return total_fee

    # Case 1
    tuition = 50000

    total1 = calculate_fee(tuition)

    print("Total Fee (Tuition Only):", total1)

    # Case 2
    hostel = 30000

    total2 = calculate_fee(tuition,
                           hostel_fee=hostel)

    print("Total Fee (Tuition + Hostel):", total2)

    # Case 3
    transport = 10000

    total3 = calculate_fee(tuition,
                           hostel_fee=hostel,
                           transportation_fee=transport)

    print("Total Fee (Tuition + Hostel + Transport):", total3)

