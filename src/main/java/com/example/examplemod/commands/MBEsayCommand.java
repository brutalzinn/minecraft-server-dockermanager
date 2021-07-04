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
import net.minecraft.util.text.ChatType;
import net.minecraft.util.text.ITextComponent;
import net.minecraft.util.text.StringTextComponent;
import net.minecraft.util.text.TranslationTextComponent;
import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class MBEsayCommand {
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
    static int sendPigLatinMessage(CommandContext<CommandSource> commandContext) throws CommandSyntaxException {
        ITextComponent messageValue = MessageArgument.getMessage(commandContext, "comando");




        Entity entity = commandContext.getSource().getEntity();
        socketClient client = new socketClient();

        if (entity != null) {
            try{
                client.startConnection("0.0.0.0", 5000);
                String response = client.sendMessage(messageValue.getString());
//                JSONParser parser = new JSONParser();
//
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
                System.out.println("Python response" + response);
            } catch (IOException e) {
                try {
                    System.out.println(e.getMessage());
                    client.stopConnection();
                } catch (IOException ioException) {
                    System.out.println(ioException.getMessage());
                }
            }

            System.out.print("Comando recebido. Se comunicando com o servidor de sockets.. enviando " + messageValue.getString() );
           // commandContext.getSource().getServer().getPlayerList().func_232641_a_(finalText, ChatType.CHAT, entity.getUniqueID());
            //func_232641_a_ is sendMessage()
        } else {
        //    commandContext.getSource().getServer().getPlayerList().func_232641_a_(finalText, ChatType.SYSTEM, Util.DUMMY_UUID);
        }
        return 1;
    }



}


