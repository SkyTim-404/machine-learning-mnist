class Option():
    def __init__(self):
        self.device = "mps"
        self.num_epochs = 200
        self.generator_learning_rate = 3e-4
        self.disciminator_learning_rate = 1e-6
        self.latent_dim = 64 # 64, 128, 256
        self.batch_size = 64
        self.generator_weight_decay = 1e-2
        self.discriminator_weight_decay = 1e-2
        
        self.load_model = True
        self.save_interval = 1
        self.discriminator_path = "weights/discriminator.pt"
        self.generator_path = "weights/generator.pt"
        self.data_path = "../../data"
        