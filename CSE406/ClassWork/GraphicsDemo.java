import java.awt.*;
import javax.swing.*;

class MyPanel extends JPanel {
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLUE);
        g.fillRect(50, 50, 100, 100);
        g.setColor(Color.RED);
        g.drawString("Hello, Graphics!", 60, 90);
    }
}



public class GraphicsDemo{
    public static void main(String[] args){
        JFrame frame = new JFrame();
        frame.add(new MyPanel());
        frame.setSize(400, 300);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}