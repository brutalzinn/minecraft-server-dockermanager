package com.example.examplemod.commands;
import com.example.examplemod.socket.socketClient;
import com.mojang.brigadier.CommandDispatcher;
import com.mojang.brigadier.builder.LiteralArgumentBuilder;
import com.mojang.brigadier.builder.RequiredArgumentBuilder;
import com.mojang.brigadier.context.CommandContext;
import com.mojang.brigadier.exceptions.CommandSyntaxException;
import net.minecraft.command.CommandSource;
import net.minecraft.command.Commands;
import net.minecraft.command.arguments.MessageArgument;
import net.minecraft.entity.Entity;
import net.minecraft.util.Util;
import net.minecraft.util.text.*;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MBEsayCommand {
    private static socketClient client = new socketClient();

    public static void register(CommandDispatcher<CommandSource> dispatcher) {
        LiteralArgumentBuilder<CommandSource> mbesayCommand
                = Commands.literal("docker")
//                .requires((commandSource) -> commandSource.hasPermission(2))
                .then(Commands.argument("comando", MessageArgument.message())
                        .executes(MBEsayCommand::sendPigLatinMessage)
                );

        dispatcher.register(mbesayCommand);
    }

    /**
     * Read the command's "message" argument, convert it to pig latin, then send as a chat message
     */
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
                return TextFormatting.GREEN + status;

            case "exited":
            case "paused":
            case "removing":
            case "dead":
                return TextFormatting.RED + status;
            default:
                return status;
        }
    }
    static String colorChangeMessageStatus(Boolean status,String data){
            if(status) {
                return TextFormatting.GREEN + "Success:" + data;
            }else{
                return TextFormatting.RED + "Error:" + data;
            }
    }

    static int sendPigLatinMessage(CommandContext<CommandSource> commandContext) throws CommandSyntaxException {
        ITextComponent messageValue = MessageArgument.getMessage(commandContext, "comando");

        Entity entity = commandContext.getSource().getEntity();

        if (entity != null) {
            new Thread(() -> {

                try{

                    System.out.print("Enviando  ao python" + messageValue.getString());

                    client.startConnection("0.0.0.0", 5000);
                    String response = client.sendMessage(messageValue.getString());
                    if(isJSONArray(response)){
                        System.out.print("This is a data array from python ");
                        StringBuilder json=new StringBuilder(response);
                        JSONObject obj=null;
                        try{
                            obj=new JSONObject(json.toString());
                            System.out.println(obj.toString());
                            JSONArray jArray = obj.getJSONArray("data");
                            entity.sendMessage(new StringTextComponent(TextFormatting.AQUA + "Name"+ " " + TextFormatting.AQUA + "Status"+ " " + TextFormatting.AQUA + "Port"),entity.getUUID());
                            for(int i = 0; i < jArray.length(); i++){
                                JSONObject o = jArray.getJSONObject(i);
                                entity.sendMessage(new StringTextComponent(TextFormatting.AQUA + o.getString("name") + " " + colorChangeTypeStatus(o.getString("status")) + " " + TextFormatting.GOLD + o.getString("port")),entity.getUUID());
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
                            entity.sendMessage(new StringTextComponent(colorChangeMessageStatus(obj.getBoolean("status"),obj.getString("data"))),entity.getUUID());
                        }catch (JSONException e){
                            e.printStackTrace();

                        }
                        System.out.print("A simple json object. " + response);

                    }
                    System.out.print("Python response " + response);
//                JSONParser parser = new JSONParser();

//                try {
//                    Object obj = parser.parse(response);
//                    JSONArray array = (JSONArray) obj;
//                    System.out.println("The 2nd element of array");
//                    System.out.println(array.get(0));
//                    System.out.println();
//
//                } catch (ParseException pe) {
//                    System.out.println("position: " + pe.getPosition());
//                    System.out.println(pe);
//                }
                } catch (IOException errore) {
                    System.out.print("ERRO:"+errore);
                    try {
                        client.stopConnection();
                    } catch (IOException ioException) {
                        ioException.printStackTrace();
                    }

//                        try {
//                            System.out.println(e.getMessage());
//                           // client.stopConnection();
//                        } catch (IOException ioException) {
//                            System.out.println(ioException.getMessage());
//                        }
                }



            }).start();


//            System.out.print("Comando recebido. Se comunicando com o servidor de sockets.. enviando " + messageValue.getString() );
           // commandContext.getSource().getServer().getPlayerList().func_232641_a_(finalText, ChatType.CHAT, entity.getUniqueID());
            //func_232641_a_ is sendMessage()
        } else {
        //    commandContext.getSource().getServer().getPlayerList().func_232641_a_(finalText, ChatType.SYSTEM, Util.DUMMY_UUID);
        }
        return 1;
    }



}


