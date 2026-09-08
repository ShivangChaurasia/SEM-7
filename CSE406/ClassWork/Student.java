import java.sql.*;
import java.util.*;


public class Student {
	int id;
	String name;
	String roll;
	String course;
	
	Student(int id, String name, String roll, String course){
		this.id = id;
		this.name= name;
		this.roll=roll;
		this.course=course;
		
	}
	
	public static void main(String args[]) {
		ArrayList<Student> students = new ArrayList<>();
		
		students.add(new Student(1, "Rahul", "101", "CSE"));
		students.add(new Student(2, "Aman", "102", "CSE"));
		students.add(new Student(3, "Shivang", "103", "CSE"));
		
		
		String url = "jdbc:mysql://localhost:3306/cse406";
		String user = "root";
		String password = "root";
		
		try {
			Connection con = DriverManager.getConnection(url, user, password);
			
			String sql = "INSERT INTO students(name, roll, course) VALUES(?,?,?)";
			
			PreparedStatement ps = con.prepareStatement(sql);
			
			for(Student s : students) {
				ps.setString(1,s.name);
                ps.setString(2, s.roll);
                ps.setString(3, s.course);

                ps.executeUpdate();
				System.out.println(s.id+" "+s.name+" "+s.roll+" "+s.course);
				
	            System.out.println("Data inserted successfully!");

	         }
			
			con.close();
	      } catch (Exception e) {
	           e.printStackTrace();
	      }
	}
}
