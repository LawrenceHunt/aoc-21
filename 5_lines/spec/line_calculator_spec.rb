require "line_calculator"
require "input_loader"

describe LineCalculator do
    subject(:line_calculator) { described_class.new() }
    let(:input_loader) { InputLoader.new("test_input_lines.txt") }
    
    describe "#add_straight_line" do
        context "given 1 line of input" do
            it "adds the line" do
                line_calculator.add_straight_line([[0,9], [5,9]])
                result = line_calculator.lines.length()
                expect(result).to eq 1
            end
        end

        context "given 2 lines of input" do
            it "ignores a non-straight line, i.e. where X1 != X2 && Y1 != Y2" do
                line_calculator.add_straight_line([[0,9], [5,9]])
                line_calculator.add_straight_line([[8,0], [0,8]])
                result = line_calculator.lines.length()
                expect(result).to eq 1
            end
        end
    end

    describe "#get_empty_grid" do
        context "given 1 line down" do
            it "draws a grid 1 by 2" do
                line_calculator.add_straight_line([[0,0], [0,1]])
                 line_calculator.get_empty_grid()
                expected_result = [[nil], [nil]]
                expect(line_calculator.grid).to eq expected_result
            end
        end
        context "given a massive grid" do
            it "draws an empty grid of the correct shape" do
                line_calculator.add_straight_line([[0,0], [0,999]])
                line_calculator.add_straight_line([[50,0], [50,2000]])
                line_calculator.get_empty_grid()
                expect(line_calculator.grid.length).to eq 2001
                expect(line_calculator.grid[0].length).to eq 51
            end
        end
    end

    describe "#draw_grid" do
        context "given 1 line down" do
            it "returns the correct grid" do
                line_calculator.add_straight_line([[0,0], [0,1]])
                line_calculator.get_empty_grid()
                result = line_calculator.draw_grid()
                expect(result).to eq [[1],[1]]
            end
        end
        
        context "given 2 lines down" do
            it "returns the correct grid" do
                line_calculator.add_straight_line([[0,0], [0,1]])
                line_calculator.add_straight_line([[0,0], [0,2]])
                line_calculator.get_empty_grid()
                result = line_calculator.draw_grid()
                expect(result).to eq [[2],[2],[1]]
            end
        end

        context "given full test input" do
            it "returns the correct grid" do
                input_loader = InputLoader.new()
                input_loader.lines.each { |line| line_calculator.add_straight_line(line) }
                line_calculator.get_empty_grid()

                expected_result = [
                    [nil, nil, nil, nil, nil, nil, nil, 1, nil, nil],
                    [nil, nil, 1, nil, nil, nil, nil, 1, nil, nil],
                    [nil, nil, 1, nil, nil, nil, nil, 1, nil, nil],
                    [nil, nil, nil, nil, nil, nil, nil, 1, nil, nil],
                    [nil, 1, 1, 2, 1, 1, 1, 2, 1, 1],
                    [nil, nil, nil, nil, nil, nil, nil, nil, nil, nil],
                    [nil, nil, nil, nil, nil, nil, nil, nil, nil, nil],
                    [nil, nil, nil, nil, nil, nil, nil, nil, nil, nil],
                    [nil, nil, nil, nil, nil, nil, nil, nil, nil, nil],
                    [2, 2, 2, 1, 1, 1, nil, nil, nil, nil],
                ]
                result = line_calculator.draw_grid()
                expect(result).to eq expected_result
            end
        end

        context "with diagonal lines active and a down-right line" do
            it "draws the correct line" do
                line_calculator.add_line([[0, 0], [2, 2]])
                line_calculator.get_empty_grid()
                line_calculator.draw_grid()
                result = line_calculator.grid
                expected_result = [
                    [1, nil, nil],
                    [nil, 1, nil],
                    [nil, nil, 1]
                ]
                expect(result).to eq expected_result
            end
        end
        
        context "with diagonal lines active and a up-right line" do
            it "draws the correct line" do
                line_calculator.add_line([[0, 2], [2, 0]])
                line_calculator.get_empty_grid()
                line_calculator.draw_grid()
                result = line_calculator.grid
                expected_result = [
                    [nil, nil, 1],
                    [nil, 1, nil],
                    [1, nil, nil]
                ]
                expect(result).to eq expected_result
            end
        end
    end

    describe "#get_points_with_2_or_more" do
        context "with full test input" do
            it "gives the correct number of points" do
                input_loader = InputLoader.new()
                input_loader.lines.each { |line| line_calculator.add_straight_line(line) }
                line_calculator.get_empty_grid()
                line_calculator.draw_grid()
                expected_result = 5
                result = line_calculator.get_points_with_2_or_more()
                expect(result).to eq expected_result
            end
        end

        context "with real input" do
            it "gives the correct number of points" do
                input_loader = InputLoader.new("input_lines.txt")
                input_loader.lines.each { |line| line_calculator.add_straight_line(line) }
                line_calculator.get_empty_grid()
                line_calculator.draw_grid()
                expected_result = 6461
                result = line_calculator.get_points_with_2_or_more()
                expect(result).to eq expected_result
            end
        end

        context "with full test input using diagonals" do
            it "gives the correct number of points" do
                input_loader = InputLoader.new()
                input_loader.lines.each { |line| line_calculator.add_line(line) }
                line_calculator.get_empty_grid()
                line_calculator.draw_grid()
                expected_result = 12
                result = line_calculator.get_points_with_2_or_more()
                expect(result).to eq expected_result
            end
        end

        context "with real input" do
            it "gives the correct number of points" do
                input_loader = InputLoader.new("input_lines.txt")
                input_loader.lines.each { |line| line_calculator.add_line(line) }
                line_calculator.get_empty_grid()
                line_calculator.draw_grid()
                expected_result = 18065
                result = line_calculator.get_points_with_2_or_more()
                expect(result).to eq expected_result
            end
        end
    end
end