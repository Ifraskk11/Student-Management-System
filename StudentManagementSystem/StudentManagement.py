from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt

console = Console()
students = {}

def header():
    console.print(Panel.fit("[bold cyan]Student Management System[/bold cyan]\nManage student records easily", border_style="cyan"))

def add_student():
    console.print("\n[bold yellow]Add New Student[/bold yellow]")
    roll = Prompt.ask("Roll Number", default="0")
    roll = int(roll)

    if roll in students:
        console.print("[red]Error: Roll number already exists![/red]")
        return

    name = Prompt.ask("Name")
    course = Prompt.ask("Course")
    students[roll] = {"name": name, "course": course}
    console.print("[green]✓ Student added successfully![/green]")

def view_all():
    if not students:
        console.print("[yellow]No students found. Add some first![/yellow]")
        return

    table = Table(title="All Students", show_lines=True, header_style="bold magenta")
    table.add_column("Roll No", style="cyan", justify="center")
    table.add_column("Name", style="green")
    table.add_column("Course", style="blue")

    for roll, data in sorted(students.items()):
        table.add_row(str(roll), data["name"], data["course"])

    console.print(table)

def search_student():
    roll = int(Prompt.ask("Enter Roll Number to search"))
    if roll in students:
        data = students[roll]
        console.print(Panel(f"[bold]Roll:[/bold] {roll}\n[bold]Name:[/bold] {data['name']}\n[bold]Course:[/bold] {data['course']}",
                           title="[green]Student Found[/green]", border_style="green"))
    else:
        console.print("[red]Student not found![/red]")

def delete_student():
    roll = int(Prompt.ask("Enter Roll Number to delete"))
    if roll in students:
        name = students[roll]["name"]
        del students[roll]
        console.print(f"[green]✓ Deleted {name} successfully![/green]")
    else:
        console.print("[red]Student not found![/red]")

def main():
    header()
    while True:
        console.print("\n[bold]Menu:[/bold]")
        console.print("1. Add Student")
        console.print("2. View All Students")
        console.print("3. Search Student")
        console.print("4. Delete Student")
        console.print("5. Exit")

        choice = Prompt.ask("Enter choice", choices=["1","2","3","4","5"])

        if choice == "1": add_student()
        elif choice == "2": view_all()
        elif choice == "3": search_student()
        elif choice == "4": delete_student()
        elif choice == "5":
            console.print("[bold cyan]Thanks for using StudentManagement! Exiting...[/bold cyan]")
            break

if __name__ == "__main__":
    main()
