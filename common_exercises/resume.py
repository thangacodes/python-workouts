print("Introuduction about myself using Python Script.\n")
while True:
    try:    
        print("1. Introduction")
        print("2. Experience")
        print("3. Technical Knowledge")
        print("4. Certification Details")
        print("5. Achivement")
        print("6. Short Term Goal")
        print("7. Long Term Goal")
        print("8. All ")
        print("9. End of Introduction")
        val = int(input("Choose title number from below list: "))
        if (val < 1 or val > 9): 
            print("Please enter value between 1 to 9 \n")
        if (val == 1):
            print("Introduction")
            print("#############")
            print("Good Morning/Afternoon/Evening All!!!")
            print("First of all thank you for giving me an oppurtunity to introduce myself\n")
            print("My name is Thangadurai. I am currently working in Financial/Banking domain. I completed B.E-Electronics and communication Engineering..")
            print("------------------------------------------------------------------")
        elif (val ==2):
            print("Experience")
            print("###############")
            print("1) I am working as a Senior Engineer-II with 12 years of work experience in AWS, Azure, Linux, Windows platforms")
            print("2) Scripting language like Shell, Bash, Python")
            print("3) Devops tools like GitHub, Jenkins, Ansible, Docker, Kubernetes, Packer, Terraform")
            print("3) Cloud domain as AWS and Azure")
            print("------------------------------------------------------------------")
        elif(val == 3):
            print("Technical Knowledge")
            print("#########################")
            print("1) I have automated daily, weekly report using Python")
            print("3) Automated OS patching activity using script and Ansible SCM which reduces time. For doing manual patching it require min 20 min to complete the task but using automation we can patch min 100+ servers in 20 min.")
            print("------------------------------------------------------------------")  
        elif(val == 4):
            print("Certification Details\n")
            print("#####################\n")
            print("1) I am a certified AWS SAA, VMWare VCP 6.5")
            print("2) Planning to write Terraform/Ansible/Kubernetes certification")
            print("------------------------------------------------------------------")
        elif(val == 5):
            print("Achivement Details")
            print("##################")
            print("1) Received appriciation mail from clients whoever i supported during my 12 years in IT tenure.")
            print("2) Have complete BE with 73% score in first class")
            print("------------------------------------------------------------------") 
        elif(val == 6):
            print("Short Term Goal")
            print("#######################")
            print("My short term goal is to become Subject Matter Expertise in devops tools like Kubernetes, Ansible, Jenkins, Terraform, AWS,Azure")
            print("------------------------------------------------------------------") 
        elif(val == 7):
            print("Long Term Goal")
            print("####################")
            print("My long term goal is to study and learn about ML/AI")
            print("------------------------------------------------------------------")  
            print("End of my Introduction")
            print("That's all about myself. Thank you All.")
            print("------------------------------------------------------------------")  
        elif(val == 8):
            title =["Introduction","experience","technical","certification","achivement","short","long","end"]
            for i in title:
                if i.lower() == "introduction":
                    print("Introduction")
                    print("####################")
                    print("Good Morning All")
                    print("First of all thank you for giving me this oppurtunity to introduce myself\n")
                    print("I am Thangadurai")
                    print("------------------------------------------------------------------")
                if i.lower() == "experience":
                    print("Experience")
                    print("####################")
                    print("1) I am working as a Senior Engineer-II with 12 years of work experience in AWS, Azure, Linux, Windows platforms")
                    print("2) Scripting language like Shell, Bash, Python")
                    print("3) Devops tools like GitHub, Jenkins, Ansible, Docker, Kubernetes, Packer, Terraform")
                    print("3) Cloud domain as AWS and Azure")
                    print("------------------------------------------------------------------")
                if i.lower() == "technical":
                    print("Technical Knowledge")
                    print("####################")
                    print("1) I have automated daily, weekly report using Python")
                    print("3) Automated OS patching activity using script and Ansible tool which reduce time. For doing manual patching it require min 20 min to complete the task but using automation we can patch min 100+ servers in 20 min.")
                    print("------------------------------------------------------------------")        
                if i.lower() == "certification":
                    print("Certification Details")
                    print("####################")
                    print("1) I am a certified AWS SAA, VMWare VCP 6.5")
                    print("2) Planning to write Terraform/Ansible/Kubernetes certification")
                    print("------------------------------------------------------------------")
                if i.lower() == "achivement":
                    print("Achivement Details")
                    print("####################")
                    print("1) Received appriciation mail from clients whoever i supported during my 12 years in IT tenure.")
                    print("2) Have complete BE with 73% score in first class")
                    print("------------------------------------------------------------------")
                if i.lower() == "short":
                    print("Short Term Goal")
                    print("####################")
                    print("My short term goal is to become Subject Matter Expertise in devops tools like Kubernetes, Ansible, Jenkins, Terraform, AWS")
                    print("------------------------------------------------------------------")   
                if i.lower() == "long":
                    print("Long Term Goal")
                    print("####################")
                    print("My long term goal is to study and learn about ML/AI")
                    print("------------------------------------------------------------------")
                if i.lower() == "end":
                    print("End of my Introduction")
                    print("####################")
                    print("Thas all about myself. Thank you All.")
                    print("------------------------------------------------------------------")  
        elif(val == 9):
            exit()
            print("Thats all about myself. Thank you All.\n")
            break
        continue
    except ValueError:
        print("Kindly enter only digits. \n")
        continue
        if (val < 1 or val > 8): 
            print("Please enter value between 1 to 8")
            break
    title =["Introduction","experience","technical","certification","achivement","short","long","end"]
    for i in title:
        if i.lower() == "introduction":
            print("Introduction \n")
            print("Good Morning All")
            print("First of all thank you for giving me an oppurtunity to introduce myself\n")
            print("I am Thangadurai")
            print("------------------------------------------------------------------")
        if i.lower() == "experience":
            print("Experience\n")
            print("1) I am working as a UNIX Admin with decade of work experience in AIX, LINUX, Windows platforms")
            print("2) Scripting language like Bash,Shell, Python")
            print("3) Devops tools like Ansible, Kubernetes, Jenkins, Terraform")
            print("3) Cloud domain AWS")
            print("------------------------------------------------------------------")
        if i.lower() == "technical":
            print("Technical Knowledge\n")
            print("1) I have automated daily, weekly report using Python")
            print("3) Automated OS patching activity using script and Ansible tool which reduce time. For doing manual patching it require min 20 min to complete the task but using automation we can patch min 100+ servers in 20 min.")
            print("------------------------------------------------------------------")        
        if i.lower() == "certification":
            print("Certification Details\n")
            print("1) I am a certified Kubetnetes, Ansible professional")
            print("2) Planning to write Terraform/Ansible/Kubernetes certification")
            print("------------------------------------------------------------------")
        if i.lower() == "achivement":
            print("Achivement Details\n")
            print("1) Received appriciation mail from clients whoever i supported during my 12 years in IT tenure.")
            print("2) Have complete BE with 73% score in first class")
            print("------------------------------------------------------------------")
        if i.lower() == "short":
            print("Short Term Goal\n")
            print("My short term goal is to become Subject Matter Expertise in devops tools like Kubernetes, Ansible, Jenkins, Terraform, AWS, Azure")
            print("------------------------------------------------------------------")   
        if i.lower() == "long":
            print("Long Term Goal\n")
            print("My long term goal is to study and learn about ML/AI")
            print("------------------------------------------------------------------")
        if i.lower() == "end":
            print("End of my Introduction")
            print("That's all about myself. Thank you All.")
            print("------------------------------------------------------------------")
