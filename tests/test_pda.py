"""
Unit tests for ECG PDA

Tests based on examples from the research paper.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from src.pda.automaton import ECGPDA


def test_pda_initialization():
    """Test PDA initializes correctly"""
    pda = ECGPDA()
    assert pda.current_state == 'q0'
    assert pda.stack == ['Z0']
    assert 'q6' in pda.F


def test_expert_complete_verification():
    """Test that expert complete pattern is accepted (Table II)"""
    pda = ECGPDA()
    expert_pattern = "O R II P Q S T V1 P Q V II ✓ V1 ✓ O"
    
    result = pda.accepts(expert_pattern)
    assert result == True, "Expert complete verification should be accepted"


def test_novice_no_verification():
    """Test that novice pattern without verification is rejected"""
    pda = ECGPDA()
    novice_pattern = "O R II P Q V1 P"
    
    result = pda.accepts(novice_pattern)
    assert result == False, "Novice pattern without verification should be rejected"


def test_stack_depth_expert():
    """Test stack depth matches paper Table IV (experts: mean 5.2)"""
    pda = ECGPDA()
    expert_pattern = "O R II P Q S T V1 P Q V II ✓ V1 ✓ O"
    
    max_depth = pda.get_max_stack_depth(expert_pattern)
    assert max_depth >= 4, "Expert should have deep stack (≥4)"


def test_stack_depth_novice():
    """Test stack depth matches paper Table IV (novices: mean 2.1)"""
    pda = ECGPDA()
    novice_pattern = "O R II P"
    
    max_depth = pda.get_max_stack_depth(novice_pattern)
    assert max_depth <= 3, "Novice should have shallow stack (≤3)"


def test_vcs_complete():
    """Test VCS for complete verification"""
    pda = ECGPDA()
    complete_pattern = "O R II P Q S T V1 P Q V II ✓ V1 ✓ O"
    
    vcs = pda.compute_vcs(complete_pattern)
    assert vcs >= 0.75, "Complete verification should have high VCS"


def test_vcs_incomplete():
    """Test VCS for incomplete verification"""
    pda = ECGPDA()
    incomplete_pattern = "O R II P Q"
    
    vcs = pda.compute_vcs(incomplete_pattern)
    assert vcs < 0.75, "Incomplete verification should have low VCS"


def test_reset_functionality():
    """Test that reset() works"""
    pda = ECGPDA()
    
    # Process some input
    pda.step('O')
    pda.step('R')
    
    # Reset
    pda.reset()
    
    assert pda.current_state == 'q0'
    assert pda.stack == ['Z0']


if __name__ == "__main__":
    print("Running tests...")
    test_pda_initialization()
    print("✓ PDA initialization")
    
    test_expert_complete_verification()
    print("✓ Expert complete verification")
    
    test_novice_no_verification()
    print("✓ Novice no verification")
    
    test_stack_depth_expert()
    print("✓ Expert stack depth")
    
    test_stack_depth_novice()
    print("✓ Novice stack depth")
    
    test_vcs_complete()
    print("✓ VCS complete")
    
    test_vcs_incomplete()
    print("✓ VCS incomplete")
    
    test_reset_functionality()
    print("✓ Reset functionality")
    
    print("\nAll tests passed! ✓")
