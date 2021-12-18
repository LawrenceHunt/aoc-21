require "input_loader"

describe InputLoader do
    subject(:input_loader) { described_class.new("test_input_lines.txt") }
    describe "#initialize" do
        context "Loading up the test file" do
            it "has the correct first line" do
                expect(input_loader.lines[0]).to eq [[0, 9], [5, 9]]
            end
        end
    end
end