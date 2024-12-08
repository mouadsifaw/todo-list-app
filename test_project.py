import project

def test_add_task():
    project.todo_list = []
    project.add_task("Learn Python")
    assert len(project.todo_list) == 1
    assert project.todo_list[0]['task'] == "Learn Python"
    assert project.todo_list[0]['completed'] == False

def test_mark_task_completed():
    project.todo_list = []
    project.add_task("Learn Python")
    project.mark_task_completed(1)
    assert project.todo_list[0]['completed'] == True

def test_invalid_task_number():
    project.todo_list = []
    project.add_task("Learn Python")
    project.mark_task_completed(2)
    assert project.todo_list[0]['completed'] == False
