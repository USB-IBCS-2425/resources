import java.awt.*;
import java.awt.image.*;
import javax.swing.ImageIcon;
import javax.imageio.ImageIO;
import java.io.File;
import java.io.IOException;
import java.awt.event.*;
import javax.swing.*;

class ImageEditing {
	private JFrame startFrame;
	private JLabel welcomeText;
	public ImageIcon icon;
	public JLabel pixelCol;
	public BufferedImage im;
	public JButton daisyButton;
	public JButton getPixel;
	public JTextField xCoord;
	public JTextField yCoord;
	public JButton change;
	public JFrame f;
	public JPanel p;
	public JLabel lab;

	public ImageEditing() {
		startFrame = new JFrame("Image Example");
		startFrame.setSize(400, 400);
		welcomeText = new JLabel("Welcome to the Image Example", JLabel.CENTER);
		welcomeText.setBounds(100, 50, 200, 40);

		startFrame.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent windowEvent){
                System.exit(0);
            }        
        });

        startFrame.add(welcomeText);
        startFrame.setLayout(null);
       

        daisyButton = new JButton("daisy!");
        daisyButton.setActionCommand("DAISY");
        daisyButton.addActionListener(new ButtonClickListener());
        daisyButton.setBounds(50, 150, 100, 40);
        startFrame.add(daisyButton);

        getPixel = new JButton("Get Pixel");
        getPixel.setActionCommand("PIX");
        getPixel.addActionListener(new ButtonClickListener());
        getPixel.setBounds(200, 150, 100, 40);
        //startFrame.add(getPixel);

        pixelCol = new JLabel("");
        pixelCol.setBounds(100, 20, 250, 40);
        xCoord = new JTextField("x");
        yCoord = new JTextField("y");
        xCoord.setBounds(220,270,40,30);
        yCoord.setBounds(260,270,40,30);
        startFrame.add(pixelCol);
        startFrame.add(xCoord);
        startFrame.add(yCoord);

        change = new JButton("go RED");
        change.setActionCommand("CHANGE");
        change.addActionListener(new ButtonClickListener());
        change.setBounds(100, 270, 60, 30);
        startFrame.add(change);

        icon = new ImageIcon("daisy.png");
        try {
        	im = ImageIO.read(new File("daisy.png"));
        }
        catch(IOException e) {
        	System.out.println("Error reading image: " + e.getMessage());
        }

        f = new JFrame();
		p = new JPanel();
		lab = new JLabel(icon);

        startFrame.setVisible(true);
	}

	public static void main(String[] args) {
		ImageEditing mWin = new ImageEditing();
	}

	private class ButtonClickListener implements ActionListener{
        public void actionPerformed(ActionEvent e) {
            String command = e.getActionCommand();  
         
            if(command.equals("DAISY"))  {
				f.add(p);
				p.add(lab);
				f.pack();
				startFrame.add(getPixel);
				f.setVisible(true);
         	}    
         	if (command.equals("PIX")) {
         		// get coordinate
         		int x = Integer.parseInt(xCoord.getText());
         		int y = Integer.parseInt(yCoord.getText());

         		int rgb = im.getRGB(x,y);
         		int r = (rgb & 0x00ff0000) >> 16;
         		int g = (rgb & 0x0000ff00) >> 8;
         		int b = rgb & 0x000000ff;
   				String myColor = "[" + r + ", " + g +", " + b + "]";
         		pixelCol.setText("Color: " + myColor);
         	}
         	if (command.equals("CHANGE")) {
         		int red = 255;
         		int green = 0;
         		int blue = 0;
         		int col = (0 << 24) | (red << 16) | (green << 8) | blue;
         		int width = im.getWidth();
         		int height = im.getHeight();
         		for (int i = 0; i < width; i++) {
         			for (int j = 0; j < height; j++) {
         				im.setRGB(i, j, col);
         			}
         		}
         		try {
         			File ofile = new File("myImage.png");
         			ImageIO.write(im, "png", ofile);
         		}
         		catch(IOException o) {
        				System.out.println("Error reading image: " + o.getMessage());
        		}
         		
         		icon = new ImageIcon(im);
         		lab.setIcon(icon);
         		lab.repaint();
         	}
      	}     
   	}
}