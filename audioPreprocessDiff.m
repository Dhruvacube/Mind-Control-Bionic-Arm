function [data,info] = audioPreprocessDiff(audioIn,info)
fs = info.SampleRate;
features = yamnetPreprocess(audioIn,fs);
data = features;
end