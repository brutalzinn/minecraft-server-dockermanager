package net.robertocpaes.dockermanager.socket;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class socketClient {
    private Socket clientSocket;
    private PrintWriter out;
    private BufferedReader in;

    public void startConnection(String ip, int port) throws IOException {
        this.clientSocket = new Socket(ip, port);
        this.out = new PrintWriter(clientSocket.getOutputStream(), true);
        this.in = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
    }
    private socketClient() {

    }
    private static socketClient instance = new socketClient();
    public static socketClient getInstance() {
        return instance;
    }
    public String sendMessage(String msg) throws IOException {

        this.out.println(msg);
        String resp = this.in.readLine();
        return resp;
    }

    public void stopConnection() throws IOException {
        this.in.close();
        this.out.close();
        this.clientSocket.close();
    }
}
