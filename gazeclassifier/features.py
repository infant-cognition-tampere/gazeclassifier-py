import saccademodel
import fixationmodel


def extract_raw_features(pointlist):
    return {
        'saccade': saccademodel.fit(pointlist),
        'fixation': fixationmodel.fit(pointlist)
    }

def extract_features(pointlist_or_raw_features):
    if isinstance(pointlist_or_raw_features, dict):
        rf = pointlist_or_raw_features
    else:
        rf = extract_raw_features(pointlist_or_raw_features)

    # Collect features
    f0_srt = len(rf['saccade']['source_points'])
    f1_sd  = len(rf['saccade']['saccade_points'])
    f2_smse = rf['saccade']['mean_squared_error']
    f3_fmse = rf['fixation']['mean_squared_error']

    return [f0_srt, f1_sd, f2_smse, f3_fmse]
