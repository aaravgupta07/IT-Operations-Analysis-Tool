try:
    file = open("02_business_data.txt", "r")
    data = file.read()
    file.close()
    lines = data.split("\n")
    print("Business data loaded successfully.")
    print()
except FileNotFoundError:
    print("Business data could not be loaded.")
    exit()

company = ""
employees = 0
software = []
hardware = []
it_support = []
issues = []
section = ""

for line in lines:
    line = line.strip()
    if line == "":
        continue
    if line == "COMPANY":
        section = "company"
    elif line == "EMPLOYEES":
        section = "employees"
    elif line == "SOFTWARE":
        section = "software"
    elif line == "HARDWARE":
        section = "hardware"
    elif line == "IT_SUPPORT":
        section = "it_support"
    elif line == "ISSUES":
        section = "issues"
    else:
        if section == "company":
            company = line
        elif section == "employees":
            employees = int(line)
        elif section == "software":
            parts = line.split(",")
            try:
                name = parts[0].strip()
                cost = int(parts[1].strip())
                software.append([name, cost])
            except (IndexError, ValueError):
                print("Invalid software entry:", line)
        elif section == "hardware":
            parts = line.split(",")
            try:
                name = parts[0].strip()
                cost = int(parts[1].strip())
                hardware.append([name, cost])
            except (IndexError, ValueError):
                print("Invalid hardware entry:", line)
        elif section == "it_support":
            parts = line.split(",")
            try:
                name = parts[0].strip()
                cost = int(parts[1].strip())
                it_support.append([name, cost])
            except (IndexError, ValueError):
                print("Invalid IT support entry:", line)
        elif section == "issues":
            parts = line.split(",")
            try:
                name = parts[0].strip()
                number = int(parts[1].strip())
                issues.append([name, number])
            except (IndexError, ValueError):
                print("Invalid issue entry:", line)

software_total = 0
for item in software:
    software_total = software_total + item[1]
highest_software = software[0]
for item in software:
    if item[1] > highest_software[1]:
        highest_software = item

hardware_total = 0
for item in hardware:
    hardware_total = hardware_total + item[1]
highest_hardware = hardware[0]
for item in hardware:
    if item[1] > highest_hardware[1]:
        highest_hardware = item

support_total = 0
for item in it_support:
    support_total = support_total + item[1]

annual_it_cost = software_total + hardware_total + support_total
monthly_it_cost = annual_it_cost / 12
cost_per_employee = annual_it_cost / employees
software_percentage = (software_total / annual_it_cost) * 100
hardware_percentage = (hardware_total / annual_it_cost) * 100
support_percentage = (support_total / annual_it_cost) * 100
highest_software_percentage = (highest_software[1] / annual_it_cost) * 100
highest_hardware_percentage = (highest_hardware[1] / annual_it_cost) * 100

total_issues = 0
highest_issue = issues[0]
for item in issues:
    total_issues = total_issues + item[1]
    if item[1] > highest_issue[1]:
        highest_issue = item

high_priority_issues = 0
medium_priority_issues = 0
low_priority_issues = 0
for item in issues:
    if item[1] >= 15:
        high_priority_issues = high_priority_issues + 1
    elif item[1] >= 10:
        medium_priority_issues = medium_priority_issues + 1
    else:
        low_priority_issues = low_priority_issues + 1

report = open("03_analysis_report.txt", "w")

report.write("IT OPERATIONS ANALYSIS REPORT\n")
report.write("=============================\n\n")

report.write("COMPANY INFORMATION\n")
report.write("--------------------\n")
report.write("Company: " + company + "\n")
report.write("Employees: " + str(employees) + "\n\n")

report.write("FINANCIAL ANALYSIS\n")
report.write("------------------\n")
report.write("Annual IT cost: $" + format(annual_it_cost, ",.2f") + "\n")
report.write("Monthly IT cost: $" + format(monthly_it_cost, ",.2f") + "\n")
report.write("IT cost per employee: $" + format(cost_per_employee, ",.2f") + "\n\n")

report.write("SPENDING BREAKDOWN\n")
report.write("------------------\n")
report.write("Software: $" + format(software_total, ",.2f") + " (" + format(software_percentage, ".1f") + "%)\n")
report.write("Hardware: $" + format(hardware_total, ",.2f") + " (" + format(hardware_percentage, ".1f") + "%)\n")
report.write("IT Support: $" + format(support_total, ",.2f") + " (" + format(support_percentage, ".1f") + "%)\n\n")

report.write("KEY FINDINGS\n")
report.write("------------\n")
report.write("Highest software expense: " + highest_software[0] + " ($" + format(highest_software[1], ",.2f") + ")\n")
report.write("Highest hardware expense: " + highest_hardware[0] + " ($" + format(highest_hardware[1], ",.2f") + ")\n")
report.write("Most common IT issue: " + highest_issue[0] + " (" + str(highest_issue[1]) + " occurrences)\n")
report.write("Total reported IT issues: " + str(total_issues) + "\n\n")

report.write("IT ISSUES PRIORITY\n")
report.write("--------------------------\n")
report.write("High-priority issues: " + str(high_priority_issues) + "\n")
report.write("Medium-priority issues: " + str(medium_priority_issues) + "\n")
report.write("Low-priority issues: " + str(low_priority_issues) + "\n\n")

report.write("IT ISSUES DETAILS\n")
report.write("-------------\n")
for item in issues:
    if item[1] >= 15:
        report.write("- " + item[0] + ": HIGH (" + str(item[1]) + " occurrences)\n")
    elif item[1] >= 10:
        report.write("- " + item[0] + ": MEDIUM (" + str(item[1]) + " occurrences)\n")
    else:
        report.write("- " + item[0] + ": LOW (" + str(item[1]) + " occurrences)\n")
report.write("\n")

report.write("SPENDING OBSERVATIONS\n")
report.write("--------------------\n")
if software_total > hardware_total and software_total > support_total:
    report.write("- Software is the largest IT spending category.\n")
elif hardware_total > software_total and hardware_total > support_total:
    report.write("- Hardware is the largest IT spending category.\n")
elif support_total > software_total and support_total > hardware_total:
    report.write("- IT support is the largest IT spending category.\n")
else:
    report.write("- Two or more IT spending categories have equal spending.\n")

if software_total > hardware_total:
    report.write("- Software spending is higher than hardware spending.\n")
elif hardware_total > software_total:
    report.write("- Hardware spending is higher than software spending.\n")
else:
    report.write("- Software and hardware spending are equal.\n")

if hardware_total > support_total:
    report.write("- Hardware spending is higher than IT support spending.\n")
elif support_total > hardware_total:
    report.write("- IT support spending is higher than hardware spending.\n")
else:
    report.write("- Hardware and IT support spending are equal.\n")

if software_total > support_total:
    report.write("- Software spending is higher than IT support spending.\n")
elif support_total > software_total:
    report.write("- IT support spending is higher than software spending.\n")
else:
    report.write("- Software and IT support spending are equal.\n")
report.write("- The largest hardware expense accounts for " + format(highest_hardware_percentage, ".1f") + "% of total IT spending.\n")
report.write("- The largest software expense accounts for " + format(highest_software_percentage, ".1f") + "% of total IT spending.\n")

report.write("\n")
report.write("MANAGEMENT FLAGS\n")
report.write("----------------\n")
flag_created = False
if highest_software[1] > 5000:
    report.write("- Review the highest software expense.\n")
    flag_created = True
if highest_hardware[1] > 5000:
    report.write("- Review the highest hardware expense.\n")
    flag_created = True
if cost_per_employee > 1800:
    report.write("- Review IT cost per employee.\n")
    flag_created = True
if software_percentage > 40:
    report.write("- Software represents more than 40% of IT spending.\n")
    flag_created = True
if hardware_percentage > 40:
    report.write("- Hardware represents more than 40% of IT spending.\n")
    flag_created = True
if support_percentage > 40:
    report.write("- Support represents more than 40% of IT spending.\n")
    flag_created = True
if highest_issue[1] >= 15:
    report.write("- Investigate the most frequently reported IT issue.\n")
    flag_created = True
if total_issues > 50:
    report.write("- Total reported IT issues exceed 50.\n")
    flag_created = True
if flag_created == False:
    report.write("- No major management flags were identified.\n")
report.close()

print("Analysis report created: 03_analysis_report.txt")