package net.robertocpaes.dockermanager;
import net.md_5.bungee.api.plugin.Plugin;
import net.robertocpaes.dockermanager.commands.DockerCommand;
import net.robertocpaes.dockermanager.files.ConfigFile;


public final class DockerManager extends Plugin{
    public ConfigFile config = new ConfigFile(this);

    @Override
    public void onEnable() {
        config.createConfig();
        getProxy().getPluginManager().registerCommand(this, new DockerCommand(this));
    }

    @Override
    public void onDisable() {
        // Plugin shutdown logic
    }
}
