from navigate.model.devices.stage.base import StageBase

class VastDevice(StageBase):
    def __init__(self, microscope_name, device_connection, configuration, device_id=0):
        super().__init__(microscope_name, device_connection, configuration, device_id)

    @property
    def commands(self):
        """Return commands dictionary

        Returns
        -------
        commands : dict
            commands that the device supports
        """
        return {"move_plugin_device": lambda *args: self.move(args[0])}

    def move(self, *args):
        """An example function: to move the device"""
        print("move device", args)
        pass

    def report_position(self):
        return self.get_position_dict()
