function [labelVals,labelLocs] = labelECGregions(x,t,parentLabelVal,parentLabelLoc,varargin)

labelVals = cell(2,1);
labelLocs = cell(2,1);

if nargin < 5
    Fs = 250;
else
    Fs = varargin{1};
end

% Download the pretrained network

netfil = matlab.internal.examples.downloadSupportFile("SPT", ...
    "data/QTDatabaseECGSegmentationNetworks.zip"); %#ok<*UNRCH>
unzip(netfil,fullfile(tempdir,"ECGnet"))
load(fullfile(tempdir,"ECGnet","trainedNetworks.mat"))
    
    for kj = 1:size(x,2)
    
        sig = x(:,kj)';
    
        predTest = classify(rawNet,sig,MiniBatchSize=50);
        
        msk = signalMask(predTest);
        msk.SpecifySelectedCategories = true;
        msk.SelectedCategories = find(msk.Categories ~= "n/a");
        
        labels = roimask(msk);
        labelVals{kj} = labels.Value;
        labelLocs{kj} = labels.ROILimits/Fs;

    end

labelVals = vertcat(labelVals{:});
labelLocs = cell2mat(labelLocs);

end