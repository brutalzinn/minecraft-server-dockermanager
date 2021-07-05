package net.robertocpaes.dockermanager.files;

import net.robertocpaes.dockermanager.DockerManager;

public class ConfigFile extends AbstractFile {

    public ConfigFile(DockerManager pl){
        super(pl, "config.yml", "/DockerManager/");
    }

    public void createConfig(){
        String lobbyServer = config.getString("lobby server");

        if (lobbyServer.equals("")){
            config.set("lobby server", "lobby");
            save();
        }
    }

}