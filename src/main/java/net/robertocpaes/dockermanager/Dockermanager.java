package net.robertocpaes.dockermanager;
import net.md_5.bungee.api.plugin.Plugin;
import net.robertocpaes.dockermanager.commands.dockerCommand;


public final class Dockermanager extends Plugin{

    @Override
    public void onEnable() {

        getProxy().getPluginManager().registerCommand(this, new dockerCommand(this));
    }

    @Override
    public void onDisable() {
        // Plugin shutdown logic
    }
}
