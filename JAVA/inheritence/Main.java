// Create a Teacher class and derive Professor/ Associate_Professor/Assistant_Professor class from Teacher class. Define appropriate constructor for all the classes. Also define a method to display information of Teacher. Make necessary assumptions as required


class Teacher {
    String name, department;
    Teacher(String name, String department) {
        this.name = name;
        this.department = department;
    }
    void displayInfo() {
        System.out.println("Name: " + name + ", Department: " + department);
    }
}
class Professor extends Teacher {
    Professor(String name, String department) { super(name, department); }
}
class Associate_Professor extends Teacher {
    Associate_Professor(String name, String department) { super(name, department); }
}
class Assistant_Professor extends Teacher {
    Assistant_Professor(String name, String department) { super(name, department); }
}
public class Main {
    public static void main(String[] args) {
        Teacher p1 = new Professor("Manav", "Information Technology");
        Teacher p2 = new Associate_Professor("Neel", "computer Science");
        Teacher p3 = new Assistant_Professor("veer", "data Science");

        p1.displayInfo();
        p2.displayInfo();
        p3.displayInfo();
    }
}