import torch.nn as nn
import numpy as np
import torch
import torch.optim as optim
import matplotlib.pyplot as plt

#Generating the data
N=100
L=1000
T=20
x=np.empty((N,L), np.float32)
x[:]=np.arange(L) + np.random.randint(-4*T,4*T,N).reshape(N,1)
y=np.sin(x/1.0/T).astype(np.float32)

plt.figure(figsize=(10,8))
plt.title('Sine wave')
plt.xlabel("x")
plt.ylabel("y")
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.plot(np.arange(x.shape[1]),y[0,:],'r',linewidth=2.0)
plt.show()



breakpoint()
 
 #LSTM model 

class LSTMPredictor(nn.Module):
    def __init__(self, hidden_layers=51):
        super(LSTMPredictor, self).__init__()
        self.hidden_layers = hidden_layers
        # lstm1, lstm2, linear are all layers in the network
        self.lstm1 = nn.LSTMCell(1, self.hidden_layers)
        self.lstm2 = nn.LSTMCell(self.hidden_layers, self.hidden_layers)
        self.linear = nn.Linear(self.hidden_layers, 1)
        
    def forward(self, y, future=0):
        outputs, n_samples = [], y.size(0)
        h_t = torch.zeros(n_samples, self.hidden_layers, dtype=torch.float32)
        c_t = torch.zeros(n_samples, self.hidden_layers, dtype=torch.float32)
        h_t2 = torch.zeros(n_samples, self.hidden_layers, dtype=torch.float32)
        c_t2 = torch.zeros(n_samples, self.hidden_layers, dtype=torch.float32)
        
        for input_t in y.split(1, dim=1):
            # N, 1
            h_t, c_t = self.lstm1(input_t , (h_t, c_t)) # initial hidden and cell states
            h_t2, c_t2 = self.lstm2(h_t, (h_t2, c_t2)) # new hidden and cell states
            output = self.linear(h_t2) # output from the last FC layer
            outputs.append(output)
            
        for i in range(future):
            # this only generates future predictions if we pass in future_preds>0
            # mirrors the code above, using last output/prediction as input
            h_t, c_t = self.lstm1(output, (h_t, c_t))
            h_t2, c_t2 = self.lstm2(h_t, (h_t2, c_t2))
            output = self.linear(h_t2)
            outputs.append(output)
        # transform list to tensor    
        outputs = torch.cat(outputs, dim=1)
        return outputs

         
if __name__ == "__main__"
    #y = (100,1000)
    train_input   = torch.from_numpy(y[3: ,  :-1])  # (97, 999)
    train_target  = torch.from_numpy(y[3: ,  1:])   # (97, 999)

    test_input   = torch.from_numpy(y[:3 ,  :-1])  # (3,  999)
    test_target  = torch.from_numpy(y[:3 ,  1:])   # (3,  999)

    model = LSTMPredictor()
    criterion = nn.MSELoss()

    optimiser = optim.LBFGS(model.parameters(), lr=0.08)

    n_epochs=10 
    for i in range(n_epochs):
        print('Step', i)

        def closure():
            optimiser.zero_grad()
            out = model(train_input)
            loss = criterion(out, train_target)
            print("loss", loss.item())
            loss.backward()
            return loss
        optimiser.step(closure)


        with torch.no_grad():
            future= 1000
            pred = model(test_input, future=future)
            # use all pred samples, but only go to 999
            loss = criterion(pred[:, :-future], test_target)
            print("test loss", loss.item())
            y = pred.detach().numpy()

        # draw figures
        plt.figure(figsize=(12,6))
        plt.title(f"Step {i+1}")
        plt.xlabel("x")
        plt.ylabel("y")
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        n = train_input.shape[1] # 999
        def draw(yi, colour):
            plt.plot(np.arange(n), yi[:n], colour, linewidth=2.0)
            plt.plot(np.arange(n, n+future), yi[n:], colour+":", linewidth=2.0)
        draw(y[0], 'r')
        draw(y[1], 'b')
        draw(y[2], 'g')
        plt.savefig("predict%d.pdf"%i)
        plt.close()

