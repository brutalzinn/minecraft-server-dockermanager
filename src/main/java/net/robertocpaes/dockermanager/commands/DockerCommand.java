package net.robertocpaes.dockermanager.commands;

import net.md_5.bungee.api.ChatColor;
import net.md_5.bungee.api.CommandSender;
import net.md_5.bungee.api.chat.TextComponent;
import net.md_5.bungee.api.config.ServerInfo;
import net.md_5.bungee.api.connection.ProxiedPlayer;
import net.md_5.bungee.api.plugin.Command;
import net.robertocpaes.dockermanager.DockerManager;
import net.robertocpaes.dockermanager.socket.socketClient;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.io.IOException;
import java.util.Arrays;

public class DockerCommand extends Command {
    private static socketClient client = new socketClient();

    private DockerManager plugin;

    public  DockerCommand(DockerManager pl) {
        super("docker", "", "doc", "d");
        plugin = pl;
    }
    static boolean isJSONValid(String test) {
        try {
            new JSONObject(test);
        } catch (JSONException ex) {
            // edited, to include @Arthur's comment
            // e.g. in case JSONArray is valid as well...
            try {
                new JSONArray(test);
            } catch (JSONException ex1) {
                return false;
            }
        }
        return true;
    }
    static boolean isJSONArray(String test) {

        StringBuilder json=new StringBuilder(test);

        try {
            JSONObject obj =new JSONObject(json.toString());
            JSONArray jArray = obj.getJSONArray("data");
            if(jArray.length() == 0){
                throw new Error("Its not json array");
            }
        } catch (JSONException ex1) {
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
            if (args.length > 0) {
                for(int i = 0; i < args.length; i++) {
                    command.append(args[i]);
                }
            }
            new Thread(() -> {
                try{
                    client.startConnection("0.0.0.0", 5000);
                    String response = client.sendMessage(command.toString());
                    if(isJSONArray(response)){
                        System.out.print("This is a data array from python ");
                        StringBuilder json=new StringBuilder(response);
                        JSONObject obj=null;
                        try{
                            obj=new JSONObject(json.toString());
                            System.out.println(obj.toString());
                            JSONArray jArray = obj.getJSONArray("data");
                            player.sendMessage(new TextComponent(ChatColor.AQUA + "Name"+ " " + ChatColor.AQUA + "Status"+ " " + ChatColor.AQUA + "Port"));
                            for(int i = 0; i < jArray.length(); i++){
                                JSONObject o = jArray.getJSONObject(i);
                                player.sendMessage(new TextComponent(ChatColor.AQUA + o.getString("name") + " " + colorChangeTypeStatus(o.getString("status")) + " " + ChatColor.GOLD + o.getString("port")));
                                System.out.println(o.getString("name"));
                            }
                        }catch(JSONException e){
                            e.printStackTrace();
                        }
                    }else{
                        StringBuilder json=new StringBuilder(response);
                        JSONObject obj=null;

                        try{
                            obj=new JSONObject(json.toString());
                            player.sendMessage(new TextComponent(colorChangeMessageStatus(obj.getBoolean("status"),obj.getString("data"))));
                        }catch (JSONException e){
                            e.printStackTrace();

                        }
                        System.out.print("A simple json object. " + response);
                    }
                    System.out.print("Python response " + response);

                } catch (IOException errore) {
                    System.out.print("ERRO:"+errore);
                    try {
                        client.stopConnection();
                    } catch (IOException ioException) {
                        ioException.printStackTrace();
                    }

                }

            }).start();
           //String lobbyServer = plugin.config.get().getString("lobby server");
         //   ServerInfo lobby = plugin.getProxy().getServerInfo(lobbyServer);
//            if (!player.getServer().getInfo().equals(lobby)){
//                player.sendMessage(new TextComponent(ChatColor.GREEN + "Teleporting to lobby..."));
//              //  player.connect(lobby);
//            }else{
                player.sendMessage(new TextComponent(ChatColor.RED + "You are already in the lobby."));

        }
    }
}