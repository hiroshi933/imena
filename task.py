with open('client_import.csv', 'r', encoding="UTF-8") as file:
    arr = file.readlines()
    result_arr = []
    for i in range(1, len(arr)):
        result = []
        data = arr[i].strip()
        data_arr = (data.split(";"))
        last_name = data_arr[0].strip()
        fio = last_name.split()
        if len(fio) > 1:
            data_arr[0] = fio[0]
            data_arr[1] = fio[1]
            data_arr[2] = fio[2]
        last_name = data_arr[0].strip()
        first_name = data_arr[1].strip()
        sur_name = data_arr[2].strip()
        gender = data_arr[3].strip()
        num = i + 1
        if gender == 'Женский' or "ж":
            gender = 2
        if gender == 'Мужской' or 'м':
            gender = 1
            phone = data_arr[4].strip().replace('(', '').replace(')', '').replace('-', '')
            avatar = data_arr[5].strip().split(('\\'))[1]
            birthday = data_arr[6].strip()
            email = data_arr[7].strip()
            data_reg = data_arr[8].strip()

            result.append(num)  # result[0]
            result.append(last_name)  # result[1]
            result.append(first_name)
            result.append(sur_name)
            result.append(gender)
            result.append(phone)
            result.append(avatar)
            result.append(birthday)
            result.append(email)
            result.append(data_reg)

        result_arr.append(result)
print(result_arr)

with open('clientservice_s_import.csv', 'r', encoding='UTF-8') as f:
    osnova = f.readlines()
    for line in osnova:
        resultativ = []
        data_osn = line.strip()
        data_ard = (data_osn.split(";"))
        name = data_ard[0].strip()
        date_old = data_ard[1].strip()
        text = data_ard[2].strip()
        for i in result_arr:
            if i[1] == name:
                num = i[0]
        resultativ.append(num)
        resultativ.append(date_old.split()[0])
        resultativ.append(date_old.split()[1])
        resultativ.append(text)
        print(resultativ)
