package net.robertocpaes.dockermanager.schema;

public class listSchema {
    public String name ;
    public String status;
    public String port;

    public listSchema() {

    }
    public listSchema(String _name, String _status,String _port) {
        this.name = _name;
        this.status = _status ;
        this.port = _port;
    }

}
