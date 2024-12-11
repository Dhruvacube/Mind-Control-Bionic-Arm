%start from here
addpath(fullfile('yamnet'))
fs = 125; %since sampled at 125Hz

adsSource = audioDatastore("D:\projects\Research\Mind Control Bionic Arm\datasets\audioFiles\",IncludeSubfolders=true,LabelSource="foldernames",FileExtensions=[".wav"]);
[adsTrain,adsValidation,adsTest] = splitEachLabel(adsSource,0.7,0.2,0.1,"randomized");

trainLabels = adsTrain.Labels;
classNames = unique(adsTrain.Labels);
numClasses = numel(classNames);
testLabels  = adsTest.Labels;

net = audioPretrainedNetwork("yamnet",NumClasses=numClasses);

% Extract features using YAMNet
adsTrain = transform(adsTrain,@audioPreprocess, "IncludeInfo",true);
adsValidation = transform(adsValidation,@audioPreprocess, "IncludeInfo",true);
adsTest = transform(adsTest,@audioPreprocess, "IncludeInfo",true);


miniBatchSize = 128;
validationFrequency = floor(numel(trainLabels)/miniBatchSize);
options = trainingOptions('sgdm', ...
    InitialLearnRate=3e-4, ...
    MaxEpochs=2, ...
    MiniBatchSize=miniBatchSize, ...
    Shuffle="every-epoch", ...
    Plots="training-progress", ...
    Metrics="accuracy", ...
    Verbose=false, ...
    LearnRateSchedule="exponential", ...
    ValidationData=adsValidation, ...
    ValidationFrequency=validationFrequency, ...
    ExecutionEnvironment="parallel-auto");

net = trainnet(adsTrain,net,"crossentropy",options);

YTest = minibatchpredict(net,adsTest);
YTestFinal = scores2label(YTest,classNames);
plotconfusion(testLabels,YTestFinal);