import os
import time
import random
from datetime import datetime


# ==========================
# USB Test Simulation
# ==========================

def simulate_progress():

    print("=== USB Auto Checker ===")
    print("Start USB test...\n")

    for i in range(101):

        print(
            f"\rTesting progress: {i:3d}%",
            end=""
        )

        time.sleep(0.03)

    print("\n")


# ==========================
# USB Test Logic
# ==========================

def usb_test():

    test_time = datetime.now()

    # 模擬 USB Device
    device_name = "SanDisk USB 3.0"


    # 模擬測試結果
    detect_result = "PASS"

    read_result = random.choice(
        ["PASS", "PASS", "PASS"]
    )

    write_result = random.choice(
        ["PASS", "FAIL"]
    )


    fail_reason = ""

    manual_check = "NO"


    if write_result == "FAIL":

        fail_reason = (
            "Write speed below threshold"
        )

        manual_check = (
            "YES - Please check USB device health manually"
        )


    result = {

        "device": device_name,

        "first_test_date":
            test_time.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "last_test_date":
            test_time.strftime(
                "%Y-%m-%d %H:%M:%S"
            ),

        "retry_count": 1,


        "detect": detect_result,

        "read_test": read_result,

        "write_test": write_result,

        "fail_reason": fail_reason,

        "manual_check": manual_check

    }


    return result



# ==========================
# HTML Report Generator
# ==========================

def generate_html(result):


    report = f"""

<!DOCTYPE html>

<html>

<head>

<title>
USB Auto Test Report
</title>


<style>

table {{

border-collapse: collapse;

width: 80%;

}}


td, th {{

border:1px solid black;

padding:8px;

}}

</style>


</head>


<body>


<h1>
USB Auto Test Report
</h1>


<h2>
Test Information
</h2>


<table>


<tr>
<th>Item</th>
<th>Result</th>
</tr>


<tr>
<td>Device</td>
<td>{result["device"]}</td>
</tr>


<tr>
<td>First Test Date</td>
<td>{result["first_test_date"]}</td>
</tr>


<tr>
<td>Last Test Date</td>
<td>{result["last_test_date"]}</td>
</tr>


<tr>
<td>Retry Count</td>
<td>{result["retry_count"]}</td>
</tr>


</table>



<h2>
Test Result
</h2>



<table>


<tr>

<th>
Test Item
</th>

<th>
Status
</th>

<th>
Reason
</th>

</tr>



<tr>

<td>
USB Detection
</td>

<td>
{result["detect"]}
</td>

<td>
-
</td>

</tr>



<tr>

<td>
Read Test
</td>

<td>
{result["read_test"]}
</td>

<td>
-
</td>

</tr>



<tr>

<td>
Write Test
</td>

<td>
{result["write_test"]}
</td>

<td>
{result["fail_reason"]}
</td>

</tr>



</table>



<h2>
Manual Inspection
</h2>


<p>

{result["manual_check"]}

</p>



</body>


</html>


"""


    desktop_path = os.path.join(

        os.path.expanduser("~"),

        "Desktop",

        "usb_test_report.html"

    )


    with open(

        desktop_path,

        "w",

        encoding="utf-8"

    ) as file:

        file.write(report)



    print(
        "HTML report generated:"
    )

    print(
        desktop_path
    )



# ==========================
# Main Program
# ==========================

if __name__ == "__main__":


    simulate_progress()


    result = usb_test()


    print("Test Result:")
    print(result)


    generate_html(result)


    print("\nUSB test completed.")