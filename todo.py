from oAuth import OAuth

account = OAuth()
todo = account.tasks()

folder_list = todo.list_folders()

for folder in folder_list:
    task_list = folder.get_tasks()
    for task in task_list:
        print(task)
        print('')