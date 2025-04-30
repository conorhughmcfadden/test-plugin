class ExampleFeature:
    def __init__(self, model, *args):
        self.model = model

        self.config_table = {
            "signal": {
                "init": self.pre_func_signal,
                "main": self.in_func_signal,
                "end": self.end_func_signal,
                "cleanup": self.cleanup_func_signal,
            },
            "data": {
                "init": self.pre_func_data,
                "main": self.in_func_data,
                "end": self.end_func_data,
                "cleanup": self.cleanup_func_data,
            },
            "node": {
                "node_type": "multi-step",  # "multi-step" or "one-step"
                "device_related": True,  # True or False
                "need_response": True,  # True or False
            },
        }

    def pre_func_signal(self):
        """Prepare device thread to run this feature"""

        galvo_stage = self.model.active_microscope.stages["z"]

        sample_rate = galvo_stage.sample_rate

        (
            exposure_times,
            sweep_times,
        ) = self.model.active_microscope.get_exposure_sweep_times()

        print(f"sample_rate: {sample_rate}\nexposure_times: {exposure_times}\nsweep_times: {sweep_times}")

    def in_func_signal(self):
        """set devices before snaping an image"""
        pass

    def end_func_signal(self):
        """decide if this feature ends after snaping an image"""
        pass

    def pre_func_data(self):
        """Prepare data thread to run this feature"""
        pass

    def in_func_data(self, frame_ids):
        """Deal with images"""
        pass

    def end_func_data(self):
        """Decide if this feature ends"""
        pass

    def cleanup_func_signal(self):
        """Cleanup"""
        pass

    def cleanup_func_data(self):
        """Cleanup"""
        pass
