import java.util.*;
import java.util.stream.Collectors;

class Student {
    String name;
    String stream;
    String department;
    double cgpa;

    public Student(String name, String stream, String department, double cgpa) {
        this.name = name;
        this.stream = stream;
        this.department = department;
        this.cgpa = cgpa;
    }

    public String getName() {
        return name;
    }

    public String getDepartment() {
        return department;
    }

    public double getCgpa() {
        return cgpa;
    }

    @Override
    public String toString() {
        return name + " (" + cgpa + ")";
    }
}

public class Q1_Streams {
    public static void main(String[] args) {
        List<Student> students = Arrays.asList(
                new Student("Aman", "BTech", "CSE", 8.5),
                new Student("Aditya", "BTech", "IT", 7.5),
                new Student("Chandan", "BTech", "CSE", 9.0),
                new Student("Shivang", "BTech", "ECE", 6.8),
                new Student("Uday", "BTech", "ME", 8.2));

        Map<Boolean, List<Student>> reportA = students.stream()
                .collect(Collectors.partitioningBy(s -> s.getCgpa() > 8.0)); //pipeline 1

        System.out.println("--- Report A: CGPA > 8.0 ---");
        System.out.println("Score > 8.0: " + reportA.get(true));
        System.out.println("Score <= 8.0: " + reportA.get(false));

        Map<String, List<Student>> reportB = students.stream()
                .collect(Collectors.groupingBy(s -> s.getDepartment())); //pipeline 2

        System.out.println("\n--- Report B: Group by Department ---");
        reportB.forEach((dept, list) -> System.out.println(dept + ": " + list));

        Map<String, List<String>> reportBNames = students.stream()
                .collect(Collectors.groupingBy(
                        s -> s.getDepartment(),
                        Collectors.mapping(s -> s.getName(), Collectors.toList())));

        System.out.println("\n--- Modified Report B: Department with Names only ---");
        reportBNames.forEach((dept, names) -> System.out.println(dept + ": " + names));
    }
}




// 4. Explain why partitioningBy()is inappropriate for Report B?
// Ans: because it is designed to split a collection into two groups based on a boolean predicate.
// In the case of Report B, we want to group students by their department, which can have multiple categories (e.g., CSE, IT, ECE, ME). ns (true and false). Instead, `groupingBy()` is the correct choice for this scenario, as it allows us to group elements based on a key (in this case, the department) and can handle multiple categories effectively.


