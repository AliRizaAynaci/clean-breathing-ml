import pickle
import pandas as pd

def main():
    with open("modelnasa01.pkl", "rb") as f:
        saved_data = pickle.load(f)

    model = saved_data["model"]
    x_test = pd.read_csv("testdatanasa.csv")
    print(model.predict(x_test))

if __name__ == "__main__":
    main()
