import os

filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input("请选择:"))
        if choice in [0, 1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input("您确定要退出系统嘛？Y/N\n")
                if answer == 'Y':
                    print("谢谢您的使用")
                    break
                else:
                    continue
            elif choice == 1:
                insert()  #录入学生信息
            elif choice == 2:
                search()  #查找学生信息
            elif choice == 3:
                delete()  #删除学生信息
            elif choice == 4:
                modify()  #修改学生信息
            elif choice == 5:
                sort()    #对学生信息排序
            elif choice == 6:
                total()   #统计学生总人数
            elif choice == 7:
                show()    #显示所有的学生信息


def menu():
    print('=====================================学生管理系统=========================================')
    print('-------------------------------------功能菜单---------------------------------------------')
    print('\t\t\t\t\t\t1.录入学生信息')
    print('\t\t\t\t\t\t2.查找学生信息')
    print('\t\t\t\t\t\t3.删除学生信息')
    print('\t\t\t\t\t\t4.修改学生信息')
    print('\t\t\t\t\t\t5.排序')
    print('\t\t\t\t\t\t6.统计学生总人数')
    print('\t\t\t\t\t\t7.显示所有学生信息')
    print('\t\t\t\t\t\t0.退出系统')
    print('-----------------------------------------------------------------------------------------')


def insert():
    student_lsit = []
    while True:
        id = input("请输入ID(如1001):")
        if not id:
            break
        name = input("请输入姓名：")
        if not name:
            break
        try:
            english = int(input("请输入英文成绩："))
            Python = int(input("请输入Python成绩："))
            Java = int(input("请输入Java成绩："))
        except:
            print("输入无效，不是整数类型，请重新输入")
            continue
        # 将录入的学生信息录入字典当中
        student = {'id': id, 'name': name, 'english': english, 'Python': Python, 'Java': Java}
        # 将学生信息添加到列表中
        student_lsit.append(student)
        answer = input("是否继续添加？Y/N\n")
        if answer == 'Y':
            continue
        else:
            break
    # 调用Save()函数，用于保存学生信息
    save(student_lsit)
    print("学生信息录入完毕！！！")


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        student_id = ''
        student_name = ''
        if os.path.exists(filename):
            mode = input("请问你是想怎么查询?\n按照ID查询输入'1', 按照姓名查询输入'2'：")
            if mode == '1':
                student_id = input("请输入学生ID：")
            elif mode == '2':
                student_name = input("请输入学生姓名：")
            else:
                print("您输入有误，请重新输入：")
                search()
            with open(filename, 'r',encoding='utf-8') as rfile:
                student_old = rfile.readlines()
                for item in student_old:
                    d = dict(eval(item))
                    if student_id != '':
                        if d['id'] == student_id:
                            student_query.append(d)
                    elif student_name != '':
                        if d['name'] == student_name:
                            student_query.append(d)
            #  显示查询结果
            show_student(student_query)
            #  清空列表
            student_query.clear()
            answer = input("是否要继续查询？Y/N\n")
            if answer == 'Y':
                continue
            else:
                break
        else:
            print("暂未保存学生信息")
            return


def show_student(lst):
    if len(lst) == 0:
        print("没有查询到学生信息，无数据显示")
        return
    #  定义标题显示格式
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^12}\t{:^10}{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    #  定义内容的显示格式
    format_data = '{:^6}\t{:^12}\t{:^10}\t{:^10}\t{:^18}{:^5}'
    for item in lst:
        print(format_data.format(item.get('id'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('Python'),
                                 item.get('Java'),
                                 int(item.get('english')) + int(item.get('Python')) + int(item.get('Java'))
                                 ))


def delete():
    while True:
        student_id = input("请输入要删除的学生的ID：")
        if student_id !='':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  #标记是否删除
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))  #将字符串转成字典
                        if d['id'] != student_id:
                            wfile.write(str(d)+'\n')
                        else:
                            flag = True
                    if flag:
                        print(f"id为{student_id}的学生信息已被删除！！！")
                    else:
                        print(f"没有找到id为{student_id}的学生信息")
            else:
                print('无学生信息！！！')
                break
            show()   # 删除之后要重新显示所有学生信息
            answer = input("是否继续删除？Y/N\n")
            if answer == 'Y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return
    student_id = input("请输入要修改的学生的ID：")
    with open(filename, 'w', encoding='utf-8') as wfile:
        for item in student_old:
            d =dict(eval(item))
            if d['id'] == student_id:
                print('找到学生信息，可以修改他的相关信息了！')
                while True:
                    try:
                        d['name'] = input('请输入姓名：')
                        d['english'] = input('请输入英文成绩：')
                        d['Python'] = input('请输入Python成绩：')
                        d['Java'] = input('请输入Java成绩：')
                    except:
                        print("您的输入有误，请重新输入！！！")
                        continue
                    else:
                        break
                wfile.write(str(d)+'\n')
                print("修改成功！！！")
            else:
                wfile.write(str(d)+'\n')
        answer = input("是否继续修改其他学生的信息？Y/N\n")
        if answer == 'Y':
            modify()


def sort():
    pass


def total():
    pass


def show():
    pass


if __name__ == '__main__':
    main()