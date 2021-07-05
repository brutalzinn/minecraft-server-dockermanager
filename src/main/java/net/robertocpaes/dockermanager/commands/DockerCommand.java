package net.robertocpaes.dockermanager.commands;

import com.google.gson.*;
import com.google.gson.reflect.TypeToken;
import net.md_5.bungee.api.ChatColor;
import net.md_5.bungee.api.CommandSender;
import net.md_5.bungee.api.chat.TextComponent;
import net.md_5.bungee.api.config.ServerInfo;
import net.md_5.bungee.api.connection.ProxiedPlayer;
import net.md_5.bungee.api.plugin.Command;
import net.robertocpaes.dockermanager.DockerManager;
import net.robertocpaes.dockermanager.schema.listSchema;
import net.robertocpaes.dockermanager.socket.socketClient;


import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class DockerCommand extends Command {

    private DockerManager plugin;

    public  DockerCommand(DockerManager pl) {
        super("docker", "", "doc", "d");
        plugin = pl;
    }

    static boolean isJSONValid(String test) {
        try {
            new Gson().fromJson(test, Object.class);
            return true;
        } catch (com.google.gson.JsonSyntaxException ex) {
            return false;
        }
    }
    static boolean isJSONArray(String test) {
        try {
            JsonParser parser = new JsonParser();
            JsonObject obj = parser.parse(test).getAsJsonObject();
            JsonArray testSuites = obj.getAsJsonArray("data");
            if (testSuites.size() > 0){
                return true;
            }
        } catch (com.google.gson.JsonSyntaxException ex1) {
            return false;
        }

        return true;
    }
    static String colorChangeTypeStatus(String status){
        switch (status){

            case "running":
            case "restarting":
                return ChatColor.GREEN + status;

            case "exited":
            case "paused":
            case "removing":
            case "dead":
                return ChatColor.RED + status;
            default:
                return status;
        }
    }
    static String colorChangeMessageStatus(Boolean status,String data){
        if(status) {
            return ChatColor.GREEN + "Success:" + data;
        }else{
            return ChatColor.RED + "Error:" + data;
        }
    }
    @Override
    public void execute(CommandSender sender, String[] args) {
        if (sender instanceof ProxiedPlayer){
            ProxiedPlayer player = (ProxiedPlayer) sender;
            plugin.config.reload();
            StringBuffer command = new StringBuffer();
            if (args.length == 0 ) {
                player.sendMessage(new TextComponent(ChatColor.RED + "É obrigatório enviar um param."));
                return;
            }
                for(int i = 0; i < args.length; i++) {
                    command.append(args[i]);
                }

            String commandSender = command.toString();
            plugin.getLogger().info("Command to send " + commandSender);

            new Thread(() -> {
                try{
                    socketClient client = socketClient.getInstance();

                    client.startConnection("0.0.0.0", 5000);
                    String response = client.sendMessage(commandSender);
                    if(isJSONArray(response)){
                        System.out.print("This is a data array from python ");
                        JsonParser parser = new JsonParser();
                        JsonObject obj = parser.parse(response).getAsJsonObject();
                        JsonArray jArray = obj.getAsJsonArray("data");
                        try{
                            player.sendMessage(new TextComponent(ChatColor.AQUA + "Name"+ " " + ChatColor.AQUA + "Status"+ " " + ChatColor.AQUA + "Port"));
                            List<listSchema> jsonObjList = new Gson().fromJson(jArray, new TypeToken<List<listSchema>>() {}.getType());
                            for(listSchema respObject : jsonObjList) {
                                player.sendMessage(new TextComponent(ChatColor.AQUA + respObject.name+ " " + colorChangeTypeStatus(respObject.status) + " " + ChatColor.GOLD + respObject.port));
                            }
                        }catch(com.google.gson.JsonSyntaxException e){
                            e.printStackTrace();
                        }
                    }else{
                        JsonParser parser = new JsonParser();
                        JsonObject obj =  parser.parse(response).getAsJsonObject();
                        try{
                            player.sendMessage(new TextComponent(colorChangeMessageStatus(obj.getAsJsonObject("status").getAsBoolean(),obj.getAsJsonObject("data").getAsString())));
                        }catch (com.google.gson.JsonSyntaxException e){
                            e.printStackTrace();

                        }
                        System.out.print("A simple json object. " + response);
                    }
                    System.out.print("Python response " + response);

                } catch (IOException errore) {
                    System.out.print("ERRO:"+errore);
//                    try {
//                        socketClient client = socketClient.getInstance();
//
//                    //    client.stopConnection();
//                    } catch (IOException ioException) {
//                        ioException.printStackTrace();
//                    }

                }

            }).start();
          //      player.sendMessage(new TextComponent(ChatColor.RED + "You are already in the lobby."));

        }
    }
}