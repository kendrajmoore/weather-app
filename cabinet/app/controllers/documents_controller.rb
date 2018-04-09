class DocumentsController < ApplicationController

  def index
  end

  def show
  end

  def new
    @docs = Docs.new
  end

  def create
    @docs = Docs.new(doc_params)

    if @docs.sav
      redirect_to @docs
    else
      render 'new'
  end

  def edit
  end

  def update
  end

  def update
  end

  def destroy
  end

  private

  def find_doc
  end

  def doc_params
    params.require(:docs).permit(:tile, :content)
  end

end
