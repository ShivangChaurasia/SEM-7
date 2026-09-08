import javax.swing.*;
import java.awt.*;
import java.awt.event.*;

public class SimpleCalculator {
    static double num1 = 0, num2 = 0;
    static String operator = "";

    public static void main(String[] args) {
        JFrame frame = new JFrame("Simple Calculator");
        frame.setLayout(new FlowLayout());

        JTextField display = new JTextField(15);
        JLabel resultLabel = new JLabel("Result: 0");
        
        frame.add(display);
        frame.add(resultLabel);

        for (int i = 0; i <= 9; i++) {
            String digit = String.valueOf(i);
            JButton numBtn = new JButton(digit);
            numBtn.addActionListener(new ActionListener() {
                public void actionPerformed(ActionEvent e) {
                    display.setText(display.getText() + digit);
                }
            });
            frame.add(numBtn);
        }

        JButton btnPlus = new JButton("+");
        JButton btnMinus = new JButton("-");
        JButton btnMul = new JButton("*");
        JButton btnDiv = new JButton("/");
        JButton btnEqual = new JButton("=");
        JButton btnClear = new JButton("C");

        frame.add(btnPlus);
        frame.add(btnMinus);
        frame.add(btnMul);
        frame.add(btnDiv);
        frame.add(btnEqual);
        frame.add(btnClear);

        btnPlus.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (!display.getText().isEmpty()) {
                    num1 = Double.parseDouble(display.getText());
                    operator = "+";
                    display.setText("");
                    resultLabel.setText("Operator: +");
                }
            }
        });

        btnMinus.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (!display.getText().isEmpty()) {
                    num1 = Double.parseDouble(display.getText());
                    operator = "-";
                    display.setText("");
                    resultLabel.setText("Operator: -");
                }
            }
        });

        btnMul.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (!display.getText().isEmpty()) {
                    num1 = Double.parseDouble(display.getText());
                    operator = "*";
                    display.setText("");
                    resultLabel.setText("Operator: *");
                }
            }
        });

        btnDiv.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (!display.getText().isEmpty()) {
                    num1 = Double.parseDouble(display.getText());
                    operator = "/";
                    display.setText("");
                    resultLabel.setText("Operator: /");
                }
            }
        });

        btnEqual.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                if (!display.getText().isEmpty() && !operator.isEmpty()) {
                    num2 = Double.parseDouble(display.getText());
                    double result = 0;

                    if (operator.equals("+")) result = num1 + num2;
                    else if (operator.equals("-")) result = num1 - num2;
                    else if (operator.equals("*")) result = num1 * num2;
                    else if (operator.equals("/")) result = (num2 != 0) ? (num1 / num2) : 0;

                    display.setText(String.valueOf(result));
                    resultLabel.setText("Result: " + result);
                    operator = "";
                }
            }
        });

        btnClear.addActionListener(new ActionListener() {
            public void actionPerformed(ActionEvent e) {
                display.setText("");
                resultLabel.setText("Result: 0");
                num1 = 0;
                num2 = 0;
                operator = "";
            }
        });

        display.addKeyListener(new KeyAdapter() {
            public void keyPressed(KeyEvent e) { 
                if (e.getKeyCode() == KeyEvent.VK_ESCAPE) {
                    display.setText("");
                    resultLabel.setText("Result: 0");
                    num1 = 0;
                    num2 = 0;
                    operator = "";
                }
            }
        });

        frame.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });

        btnPlus.addMouseListener(new MouseAdapter() {
            public void mouseEntered(MouseEvent e) {
                resultLabel.setText("Mouse entered + button");
            }
        });

        frame.setSize(220, 300);
        frame.setVisible(true);
    }
}
