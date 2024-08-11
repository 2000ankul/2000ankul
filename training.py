from src.pipeline.training import Training
from flask import Flask

app = Flask(__name__)


def main():
        training = Training()
        res = training.initiate_model_training()
        print(res)    


if __name__ == "__main__":
    main()
#     app.run(debug=True)