import torch
import torch.nn as nn
import torch.optim as optim
import torchvision 
import torchvision.transforms as transforms
from torchvision.utils import save_image
import os
# Set output directory
os.makedirs("gan_outputs", exist_ok=True)
# Hyperparameters
latent_dim = 100
batch_size = 64
lr = 0.0002
epochs = 10
# Data loading
transform = transforms.Compose([transforms.ToTensor(),transforms.Normalize([0.5], [0.5])])
train_loader = torch.utils.data.DataLoader(torchvision.datasets.MNIST(root='./data', train=True, transform=transform, download=True),batch_size=batch_size, shuffle=True)
# Generator
class Generator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(nn.Linear(latent_dim, 256),nn.LeakyReLU(0.2),nn.Linear(256, 512),nn.LeakyReLU(0.2),nn.Linear(512, 1024),nn.LeakyReLU(0.2),nn.Linear(1024, 28*28),nn.Tanh())
        def forward(self, z):
            return self.model(z).view(-1, 1, 28, 28)
# Discriminator
class Discriminator(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(nn.Flatten(),nn.Linear(28*28, 512),nn.LeakyReLU(0.2),nn.Linear(512, 256),nn.LeakyReLU(0.2),nn.Linear(256, 1),nn.Sigmoid())
        def forward(self, x):
            return self.model(x)
# Initialize
G = Generator()
D = Discriminator()
criterion = nn.BCELoss()
opt_G = optim.Adam(G.parameters(), lr=lr)
opt_D = optim.Adam(D.parameters(), lr=lr)

# Training
for epoch in range(epochs):
    for i, (imgs, _) in enumerate(train_loader):
        valid = torch.ones(imgs.size(0), 1)
        fake = torch.zeros(imgs.size(0), 1)
# Generator
opt_G.zero_grad()
z = torch.randn(imgs.size(0), latent_dim)
gen_imgs = G(z)
g_loss = criterion(D(gen_imgs), valid)
g_loss.backward()
opt_G.step()

# Discriminator
opt_D.zero_grad()
real_loss = criterion(D(imgs), valid)
fake_loss = criterion(D(gen_imgs.detach()), fake)
d_loss = (real_loss + fake_loss) / 2
d_loss.backward()
opt_D.step()
if i % 200 == 0:
    print(f"Epoch {epoch} Batch {i} | D Loss: {d_loss.item():.4f} | G Loss: {g_loss.item():.4f}")
    save_image(gen_imgs[:25], f"gan_outputs/epoch{epoch}_batch{i}.png", nrow=5, normalize=True)