
with open("logs.txt", "r") as log_file:
    logs=log_file.readlines()

    print("="*40)
    print("Python Security Log Analyzer")
    print("=" * 40)
    total_alerts=0
    alert_list={}
    ip_list = {}

#reading logs
    for alert in logs:
        if "[**]" not  in alert:
          continue
        parts=alert.split("[**]")
        if len(parts)<2:
            continue
        alert_block=parts[1]
        alert_name=alert_block.split("]")[-1].strip()
        total_alerts+=1
        if alert_name not in alert_list:
            alert_list[alert_name]=1
        else:
            alert_list[alert_name]+=1
#reading ips from logs
    for ips in logs:
        if "->" not in ips:
            continue

        ip_part = ips.split("}")[1].strip()

        main_ip = ip_part.split("->")[0].strip()

        if main_ip not in ip_list:
            ip_list[main_ip] = 1
        else:
            ip_list[main_ip] += 1
#making report
    report = open("report.txt", "w")
    report.write("Python Security Log Report\n")
    report.write("=" * 30 + "\n\n")
    for k in alert_list:
        report.write(f" {k} : {alert_list[k]}\n")

    for ip in ip_list:
        report.write(f"{ip} : {ip_list[ip]}\n")

    report.write(f"\nTotal Alerts :{total_alerts}")
    report.close()