with open("fileprocessor.input", "r") as file:
    lines = file.readlines()

for line in lines:
    if line.startswith('#'):
        print(f"{line} is skipped because it starts with a hashtag (is commented out)")
        continue
    user_infos = line.strip().split(':')
    if len(user_infos) == 4:
         username, password, userid, groupid = user_infos
         print(f"The user {username} has a password of {password} and has userid {userid} and groupid {groupid}")
    else:
        print("No values, program ends")
print("\nEnd of User Data")
