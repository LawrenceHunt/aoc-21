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

    describe "#draw_grid" do
        context "given 1 line down" do
            it "returns the correct grid" do
                line_calculator.add_straight_line([[0,0], [0,1]])
                result = line_calculator.draw_grid()
                expect(result).to eq [[1],[1]]
            end
        end
        
        context "given 2 lines down" do
            it "returns the correct grid" do
                line_calculator.add_straight_line([[0,0], [0,1]])
                line_calculator.add_straight_line([[0,0], [0,2]])
                result = line_calculator.draw_grid()
                expect(result).to eq [[2],[2],[1]]
            end
        end

        # context "given 2 overlapping lines of input" do
        #     it "returns 0" do
        #         line_calculator.add_straight_line([[2,2], [2,4]])
        #         line_calculator.add_straight_line([[1,3], [3,3]])
        #         result = line_calculator.calculate_overlap()
        #         expect(result).to eq 0
        #     end
        # end
    end
end