#!/usr/bin/env python3
"""
Compatibility Checker for arche Mode Combinations

This tool validates that a proposed combination of modes in a Multi-Agent Organization (MAO)
is compatible and provides recommendations.

Usage:
    python arche_compat_check.py --modes 3-layer rl-loop agentic-swarm
    python arche_compat_check.py --config mao-config.yaml
"""

import sys
import argparse
from typing import Set, List, Dict, Tuple
from dataclasses import dataclass


@dataclass
class CompatibilityScore:
    """Represents compatibility between two modes"""
    modes: Tuple[str, str]
    score: int  # 1-5: 1=poor, 5=excellent
    color: str  # For display: green/yellow/red
    patterns: List[str]  # Known successful patterns
    warnings: List[str]  # Potential issues
    recommendations: List[str]  # How to make it work


class ArcheCompatibilityChecker:
    """Validates mode combinations and provides guidance"""
    
    # Compatibility matrix from MODE_COMPATIBILITY.md
    COMPATIBILITY_MATRIX = {
        ("3-layer", "3-layer"): CompatibilityScore(
            modes=("3-layer", "3-layer"),
            score=5,
            color="🟢",
            patterns=["Sequential routing", "Multiple deterministic agents"],
            warnings=[],
            recommendations=["Use for deterministic workflows", "Each agent owns clear responsibility"]
        ),
        ("3-layer", "rl-loop"): CompatibilityScore(
            modes=("3-layer", "rl-loop"),
            score=5,
            color="🟢",
            patterns=["Rule-based fallback to learned policy", "Gradual migration"],
            warnings=[],
            recommendations=["Start with 3-Layer rules", "Blend in RL-Loop learning gradually", "See MODE_MIGRATION_GUIDE.md"]
        ),
        ("3-layer", "event-driven"): CompatibilityScore(
            modes=("3-layer", "event-driven"),
            score=4,
            color="🟢",
            patterns=["Event handlers with deterministic logic"],
            warnings=["Latency-sensitive events may struggle"],
            recommendations=["Use 3-Layer for complex event handlers", "Event-Driven for routing", "Monitor handler latency"]
        ),
        ("3-layer", "agentic-swarm"): CompatibilityScore(
            modes=("3-layer", "agentic-swarm"),
            score=5,
            color="🟢",
            patterns=["Coordinator with 3-Layer sub-agents", "Specialist teams"],
            warnings=[],
            recommendations=["3-Layer for each specialist", "Agentic-Swarm for coordination", "Clear role boundaries"]
        ),
        ("3-layer", "foundry"): CompatibilityScore(
            modes=("3-layer", "foundry"),
            score=5,
            color="🟢",
            patterns=["Foundry generates 3-Layer agents", "Deterministic MAO scaffolding"],
            warnings=[],
            recommendations=["Foundry creates 3-Layer agents", "Good for simple MAOs", "See MODE_INTEGRATION_GUIDE.md"]
        ),
        ("rl-loop", "rl-loop"): CompatibilityScore(
            modes=("rl-loop", "rl-loop"),
            score=4,
            color="🟢",
            patterns=["Multiple learning agents", "Shared reward signal"],
            warnings=["Reward signal must align across agents"],
            recommendations=["Define unified reward", "Monitor for policy conflicts", "Centralize feedback collection"]
        ),
        ("rl-loop", "event-driven"): CompatibilityScore(
            modes=("rl-loop", "event-driven"),
            score=4,
            color="🟢",
            patterns=["Event-triggered learning updates", "Real-time outcome logging"],
            warnings=[],
            recommendations=["Event-Driven for ingestion", "RL-Loop in handlers", "Log all decisions for learning"]
        ),
        ("rl-loop", "agentic-swarm"): CompatibilityScore(
            modes=("rl-loop", "agentic-swarm"),
            score=3,
            color="🟡",
            patterns=["Swarm with learning agents", "Coordination + adaptation"],
            warnings=["Coordination overhead", "Learning may create conflicting policies", "Credit assignment complex"],
            recommendations=["Define clear agent responsibilities", "Shared reward preferred", "Monitor convergence"]
        ),
        ("rl-loop", "foundry"): CompatibilityScore(
            modes=("rl-loop", "foundry"),
            score=5,
            color="🟢",
            patterns=["Foundry generates learning MAOs", "Adaptive scaffold generation"],
            warnings=[],
            recommendations=["Foundry + RL-Loop for self-improving MAOs", "Strong learning signal needed"]
        ),
        ("event-driven", "event-driven"): CompatibilityScore(
            modes=("event-driven", "event-driven"),
            score=4,
            color="🟢",
            patterns=["Event pipeline with multiple handlers", "Cascading events"],
            warnings=["Can become complex", "Ordering dependencies"],
            recommendations=["Document event flow", "Use event routing layer", "Monitor for event storms"]
        ),
        ("event-driven", "agentic-swarm"): CompatibilityScore(
            modes=("event-driven", "agentic-swarm"),
            score=4,
            color="🟢",
            patterns=["Event dispatcher + swarm handlers", "Reactive coordination"],
            warnings=[],
            recommendations=["Event-Driven for ingestion", "Agentic-Swarm for handling", "Decouple with event queue"]
        ),
        ("event-driven", "foundry"): CompatibilityScore(
            modes=("event-driven", "foundry"),
            score=4,
            color="🟢",
            patterns=["Foundry generates event handlers", "Reactive MAO scaffolding"],
            warnings=[],
            recommendations=["Good for reactive MAOs", "See MODE_INTEGRATION_GUIDE.md"]
        ),
        ("agentic-swarm", "agentic-swarm"): CompatibilityScore(
            modes=("agentic-swarm", "agentic-swarm"),
            score=3,
            color="🟡",
            patterns=["Meta-coordination", "Hierarchical swarms"],
            warnings=["Coordination overhead grows", "Message passing can bottleneck"],
            recommendations=["Limit hierarchy depth", "Use clear protocols", "Monitor message volume"]
        ),
        ("agentic-swarm", "foundry"): CompatibilityScore(
            modes=("agentic-swarm", "foundry"),
            score=5,
            color="🟢",
            patterns=["Foundry generates coordinating swarms", "Complex MAO scaffolding"],
            warnings=[],
            recommendations=["Good for complex MAOs", "Foundry orchestrates specialists"]
        ),
        ("foundry", "foundry"): CompatibilityScore(
            modes=("foundry", "foundry"),
            score=2,
            color="🔴",
            patterns=[],
            warnings=["Foundry generates MAOs; nesting not recommended"],
            recommendations=["Use Foundry once at top level", "Individual agents use other modes"]
        ),
    }
    
    def check_combination(self, modes: List[str]) -> Dict:
        """Check compatibility of a list of modes"""
        modes = [m.lower() for m in modes]
        results = {
            "modes": modes,
            "pairwise_results": [],
            "overall_score": 0,
            "warnings": [],
            "recommendations": [],
            "valid": True
        }
        
        # Check each pair
        scores = []
        for i, mode1 in enumerate(modes):
            for mode2 in modes[i+1:]:
                pair = tuple(sorted([mode1, mode2]))
                compat = self._get_compatibility(pair)
                
                if compat is None:
                    results["valid"] = False
                    results["warnings"].append(f"Unknown modes: {pair}")
                    continue
                
                scores.append(compat.score)
                results["pairwise_results"].append({
                    "modes": pair,
                    "score": compat.score,
                    "color": compat.color,
                    "patterns": compat.patterns,
                    "warnings": compat.warnings,
                    "recommendations": compat.recommendations
                })
        
        # Foundry special case: should only be used once
        if modes.count("foundry") > 1:
            results["valid"] = False
            results["warnings"].append("⚠️  Foundry mode listed multiple times - should only appear once at top level")
        
        # Overall score is minimum of pairwise scores
        if scores:
            results["overall_score"] = min(scores)
        
        # Aggregate recommendations
        if results["pairwise_results"]:
            for result in results["pairwise_results"]:
                results["recommendations"].extend(result["recommendations"])
            results["recommendations"] = list(set(results["recommendations"]))  # deduplicate
        
        return results
    
    def _get_compatibility(self, mode_pair: Tuple[str, str]) -> CompatibilityScore:
        """Get compatibility score for a mode pair"""
        # Try both orderings
        forward = self.COMPATIBILITY_MATRIX.get(mode_pair)
        if forward:
            return forward
        
        reverse = (mode_pair[1], mode_pair[0])
        return self.COMPATIBILITY_MATRIX.get(reverse)
    
    def print_report(self, results: Dict) -> None:
        """Pretty-print compatibility report"""
        print("\n" + "="*70)
        print(f"ARCHE MODE COMPATIBILITY REPORT")
        print("="*70)
        
        print(f"\nModes analyzed: {', '.join(results['modes'])}")
        
        if not results["valid"]:
            print("\n⚠️  VALIDATION ISSUES:")
            for warning in results["warnings"]:
                print(f"  • {warning}")
        
        if results["overall_score"]:
            score_color = "🟢" if results["overall_score"] >= 4 else "🟡" if results["overall_score"] >= 3 else "🔴"
            score_text = {5: "Excellent", 4: "Good", 3: "Fair", 2: "Poor", 1: "Incompatible"}
            print(f"\nOverall Compatibility: {score_color} {score_text.get(results['overall_score'], 'Unknown')} ({results['overall_score']}/5)")
        
        if results["pairwise_results"]:
            print("\nPairwise Compatibility:")
            print("-" * 70)
            for result in results["pairwise_results"]:
                modes_str = " ↔ ".join(result["modes"])
                score_text = {5: "Excellent", 4: "Good", 3: "Fair", 2: "Poor", 1: "Incompatible"}
                print(f"\n{result['color']} {modes_str}: {score_text[result['score']]}")
                
                if result["warnings"]:
                    print("  Warnings:")
                    for warning in result["warnings"]:
                        print(f"    ⚠️  {warning}")
                
                if result["patterns"]:
                    print("  Known patterns:")
                    for pattern in result["patterns"]:
                        print(f"    ✓ {pattern}")
        
        if results["recommendations"]:
            print("\n" + "-" * 70)
            print("RECOMMENDATIONS:")
            for i, rec in enumerate(results["recommendations"], 1):
                print(f"  {i}. {rec}")
        
        print("\n" + "="*70)
        if results["valid"] and results["overall_score"] >= 3:
            print("✓ This combination is viable. See recommendations above.")
        elif results["valid"]:
            print("⚠️  This combination is possible but has challenges.")
        else:
            print("✗ This combination has validation issues. Review above.")
        print("="*70 + "\n")


def main():
    parser = argparse.ArgumentParser(
        description="Check compatibility of arche mode combinations"
    )
    parser.add_argument(
        "--modes",
        nargs="+",
        help="List of modes to check (e.g., --modes 3-layer rl-loop)"
    )
    parser.add_argument(
        "--list",
        action="store_true",
        help="List all available modes"
    )
    
    args = parser.parse_args()
    
    checker = ArcheCompatibilityChecker()
    
    if args.list:
        modes = sorted(set(m[0] for m in checker.COMPATIBILITY_MATRIX.keys()))
        print("\nAvailable modes in arche:")
        for mode in modes:
            print(f"  • {mode}")
        print()
        return
    
    if not args.modes:
        parser.print_help()
        return
    
    results = checker.check_combination(args.modes)
    checker.print_report(results)
    
    # Return exit code based on validity
    sys.exit(0 if results["valid"] else 1)


if __name__ == "__main__":
    main()
