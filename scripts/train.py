import torch
import torch.nn as nn
import torch.nn.functional as F
from model import Net
from tqdm import tqdm
import torch.optim as optim
from data import get_xy
from dataset import CustomDataset
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt
from IPython.display import clear_output

inputs,targets = get_xy()
domain = list(set(targets))
csize = (len(domain))

mtot = {str(m):t for t,m in enumerate(domain)}
ttom = {t:m for m,t in mtot.items()}
encode = lambda targets: [mtot[str(m)] for m in targets]
decode = lambda tokens: [ttom[t] for t in tokens]
targets = torch.tensor(encode(targets[:500000]),dtype = torch.int64)
inputs = torch.tensor(inputs[:500000],dtype = torch.float32)

targets = F.one_hot(targets).to(torch.float32)



device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
model = Net(csize)
model = model.to(device)
batch_size = 64
optimizer = optim.Adam(model.parameters(), lr=1e-4)
loss_f = nn.CrossEntropyLoss()




def train(model, device, train_loader, optimizer, epochs):
    model.train()
    loss_counter = []
    for epoch in tqdm(range(epochs)):
        
        for batch_idx, (data, target) in enumerate((train_loader)):
            if batch_idx+1 == len(train_loader):
                continue
            data, target = data.to(device), target.to(device)
            optimizer.zero_grad()
            output = model(data)
#             print(output.shape)
            loss = loss_f(output, target)
            
            loss.backward()
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            
            optimizer.step()
            if batch_idx % 1000 == 0:
                print('Train Epoch: {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(
                    epoch, batch_idx * len(data), len(train_loader.dataset),
                    100. * batch_idx / len(train_loader), loss.item()))
            loss_counter.append(loss.item())
        clear_output(wait=True)
            
    
    # Plot loss
    plt.plot(loss_counter)
    plt.xlabel('Iterations')
    plt.ylabel('Loss')
    plt.title('Training Loss')
    plt.show()

def main():
    dataset = CustomDataset(inputs,targets)
    train_loader = DataLoader(dataset,batch_size,shuffle=True)
    train(model,device,train_loader,optimizer,epochs=50)
    torch.save(model.state_dict(), "models/model.pth")

if __name__ == "__main__":
    main()