import javax.swing.*;

public class Form {

    public static void main(String[] args) {

        // 1. Create JFrame (main window)
        JFrame frame = new JFrame("Student Registration Form");

        // 2. Set size of window
        frame.setSize(500, 400);

        // 3. Close the program when X is clicked
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // 4. Create JPanel
        JPanel panel = new JPanel();

        // 5. Create and add Name components
        JLabel nameLabel = new JLabel("Name: ");
        JTextField nameField = new JTextField(20);

        panel.add(nameLabel);
        panel.add(nameField);

        // 6. Create and add Roll Number components
        JLabel rollLabel = new JLabel("Roll No: ");
        JTextField rollField = new JTextField(20);

        panel.add(rollLabel);
        panel.add(rollField);

        // 7. Create and add Course components
        JLabel courseLabel = new JLabel("Course: ");

        JComboBox<String> courseBox =
                new JComboBox<>(new String[]{"Java", "Python", "C++"});

        panel.add(courseLabel);
        panel.add(courseBox);

        // 8. Create and add Gender components
        JLabel genderLabel = new JLabel("Gender: ");

        JRadioButton male = new JRadioButton("Male");
        JRadioButton female = new JRadioButton("Female");

        // Make Male and Female mutually exclusive
        ButtonGroup genderGroup = new ButtonGroup();
        genderGroup.add(male);
        genderGroup.add(female);

        panel.add(genderLabel);
        panel.add(male);
        panel.add(female);

        // 9. Create and add Email components
        JLabel emailLabel = new JLabel("Email: ");
        JTextField emailField = new JTextField(20);

        panel.add(emailLabel);
        panel.add(emailField);

        // 10. Create buttons
        JButton registerButton = new JButton("Register");
        JButton clearButton = new JButton("Clear");

        panel.add(registerButton);
        panel.add(clearButton);

        // 11. Add JPanel to JFrame
        frame.add(panel);

        // 12. Make JFrame visible
        frame.setVisible(true);
    }
}