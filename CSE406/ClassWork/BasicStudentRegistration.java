import java.awt.*;
import javax.swing.*;

public class BasicStudentRegistration {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Student Registration Form");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.setLayout(new GridLayout(4, 2, 10, 10));

        frame.add(new JLabel(" Student Name:"));
        frame.add(new JTextField());

        frame.add(new JLabel(" Roll Number:"));
        frame.add(new JTextField());

        frame.add(new JLabel(" Course:"));
        frame.add(new JTextField());

        frame.add(new JLabel(""));
        frame.add(new JButton("Register"));
    }
}
