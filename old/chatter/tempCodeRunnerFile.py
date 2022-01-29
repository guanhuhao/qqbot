for files in os.listdir(trainingSet):
    trainer.train(trainingSet+files)
    print(trainingSet+files)