class ApiPlayerCameraSettings:

    def __init__(self, stiffness: float = None, height: float = None, transition_speed: float = None,
                 pitch: float = None, swivel_speed: float = None, field_of_view: float = None, distance: float = None):
        self.stiffness = stiffness
        self.height = height
        self.transition_speed = transition_speed
        self.pitch = pitch
        self.swivel_speed = swivel_speed
        self.field_of_view = field_of_view
        self.distance = distance

    @staticmethod
    def create_from_player(proto_camera, player):
        player_camera_settings = player.camera_settings
        if player.camera_settings['stiffness'] is None:
            return

        proto_camera.stiffness = player_camera_settings['stiffness']
        proto_camera.height = player_camera_settings['height']
        proto_camera.transition_speed = player_camera_settings['transition_speed']
        proto_camera.pitch = player_camera_settings['pitch']
        proto_camera.swivel_speed = player_camera_settings['swivel_speed']
        proto_camera.field_of_view = player_camera_settings['field_of_view']
        proto_camera.distance = player_camera_settings['distance']
