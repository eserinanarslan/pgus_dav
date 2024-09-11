import unittest
import pandas as pd
import numpy as np

# Define the function to be tested
def calc_label_score(final_df):
    # Calculate the Label_Score by taking a weighted sum of probabilities from three models
    final_df['Label_Score'] = ((final_df['rf_prob']*0.71) + 
                               (final_df['nb_prob']*0.63) + 
                               (final_df['cnb_prob']*0.64))
    
    # Define a normalization function that scales the data between 0 and 1
    def NormalizeData(data):
        return (data - np.min(data)) / (np.max(data) - np.min(data))
    
    # Apply the normalization function to 'Label_Score' and round the result to 2 decimal places
    final_df['Label_Score'] = NormalizeData(final_df['Label_Score']).round(2)
    
    # Return the modified DataFrame
    return final_df

class TestCalcLabelScore(unittest.TestCase):
    def setUp(self):
        # Sample data for testing
        self.df = pd.DataFrame({
            'rf_prob': [0.1, 0.5, 0.9],
            'nb_prob': [0.2, 0.6, 0.8],
            'cnb_prob': [0.3, 0.7, 0.6]
        })
        
        # Calculate expected Label_Score manually
        self.df['Label_Score'] = ((self.df['rf_prob']*0.71) + 
                                  (self.df['nb_prob']*0.63) + 
                                  (self.df['cnb_prob']*0.64))
        
        # Normalize and round the expected Label_Score
        min_score = self.df['Label_Score'].min()
        max_score = self.df['Label_Score'].max()
        self.df['Label_Score'] = (self.df['Label_Score'] - min_score) / (max_score - min_score)
        self.df['Label_Score'] = self.df['Label_Score'].round(2)
        
        # Expected DataFrame
        self.expected_df = self.df.copy()

    def test_calc_label_score(self):
        # Apply the function
        result_df = calc_label_score(pd.DataFrame({
            'rf_prob': [0.1, 0.5, 0.9],
            'nb_prob': [0.2, 0.6, 0.8],
            'cnb_prob': [0.3, 0.7, 0.6]
        }))
        
        # Check if the result matches the expected DataFrame
        pd.testing.assert_frame_equal(result_df, self.expected_df, check_dtype=False)

if __name__ == '__main__':
    unittest.main()
