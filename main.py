"""CLI Logic"""
import sys
import task_tracker

def main():
    """main function"""
    args = sys.argv[1:]
    if not args:
        print("Usage: task-cli <command> [arguments]")
        return
    command = args[0]
    if command == "add":
        if len(args) < 2:
            print("Usage: task-cli add <description>")
        else:
            task_tracker.add_task(args[1])
    elif command == "update":
        if len(args) < 3:
            print("Usage: task-cli update <description>")
        else:
            task_tracker.update_task(int(args[1]), args[2])
    elif command == "delete":
        if len(args) < 2:
            print("Usage: task-cli delete <id>")
        else:
            task_tracker.delete_task(int(args[1]))
    elif command in ["mark-todo", "mark-in-progress", "mark-done"]:
        if len(args) < 2:
            print(f"Usage: task-cli {command} <id>")
        else:
            status = command.split("-")[1]
            task_tracker.change_status(int(args[1]), status)
    elif command == "list":
        status = args[1] if len(args) > 1 else None
        task_tracker.list_tasks(status)
    else:
        print(f"Unkown command: {command}")

if __name__ == "__main__":
    main()
