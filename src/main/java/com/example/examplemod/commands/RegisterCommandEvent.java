package com.example.examplemod.commands;
import com.mojang.brigadier.CommandDispatcher;
import net.minecraft.command.CommandSource;
import net.minecraftforge.event.RegisterCommandsEvent;
import net.minecraftforge.eventbus.api.SubscribeEvent;
import net.minecraftforge.fml.event.server.FMLServerStartingEvent;

/**
 * User: The Grey Ghost
 * Date: 24/12/2014
 *
 * Register our commands when the server starts up.
 *
 * Don't forget to register this class on the MinecraftForge.EVENT_BUS.
 */
public class RegisterCommandEvent
{
    @SubscribeEvent
    public static void onRegisterCommandEvent(RegisterCommandsEvent event) {
        CommandDispatcher<CommandSource> commandDispatcher = event.getDispatcher();
        MBEsayCommand.register(commandDispatcher);
//        MBEquoteCommand.register(commandDispatcher);
    }
}
