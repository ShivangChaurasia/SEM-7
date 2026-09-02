import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JTextField;

public class Form {
	
	public static void main(String args[]) {
		JFrame frame = new JFrame("Employee Registration Form");
        frame.setSize(300, 200);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.setLayout(new GridLayout(4, 2, 10, 10));

        frame.add(new JLabel("Employee Name:"));
        frame.add(new JTextField());

        frame.add(new JLabel("Employee ID"));
        frame.add(new JTextField());

        frame.add(new JLabel("Department"));
        frame.add(new JTextField());

        frame.add(new JLabel(""));
        frame.add(new JButton("Register"));
        
        frame.setVisible(true);
	}

}	
